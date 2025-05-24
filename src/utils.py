import subprocess
import logging
import re



# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_service_name(server_name):
    """Get the appropriate service name based on the server type."""
    if server_name == "palworld":
        return "palworld.service"
    return f"docker-compose@{server_name}.service"

def run_systemctl_command(command, service):
    """Run a systemctl command with proper error handling."""
    try:
        # Check if we need sudo (usually required for systemctl)
        import os
        use_sudo = os.geteuid() != 0  # Will be True if not running as root
        
        cmd = []
        if use_sudo:
            cmd.append("sudo")
        
        cmd.extend(["systemctl", command, service])
        
        # Log the command being executed
        logger.info(f"Executing: {' '.join(cmd)}")
        
        # Use explicit array to avoid shell injection
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False  # Don't raise exception so we can handle it ourselves
        )
        
        # Log the result
        if result.returncode != 0:
            logger.error(f"Command failed with return code {result.returncode}")
            logger.error(f"Stderr: {result.stderr}")
            logger.error(f"Stdout: {result.stdout}")
        else:
            logger.info(f"Command succeeded")
            
        return result
    except Exception as e:
        logger.exception(f"Exception executing systemctl {command}: {str(e)}")
        # Create a result-like object with error info
        class ErrorResult:
            def __init__(self, error):
                self.returncode = 1
                self.stdout = ""
                self.stderr = str(error)
        return ErrorResult(e)

def start_server(server_name):
    """Start the specified server."""
    service = get_service_name(server_name)
    return run_systemctl_command("start", service)

def stop_server(server_name):
    """Stop the specified server."""
    service = get_service_name(server_name)
    return run_systemctl_command("stop", service)

def restart_server(server_name):
    """Restart the specified server."""
    service = get_service_name(server_name)
    return run_systemctl_command("restart", service)

def check_status(server_name):
    """Get a cleaned and parsed status using both `systemctl show` and `status`."""
    service = get_service_name(server_name)

    # Run `systemctl show`
    show_result = run_systemctl_command("show", service)
    if show_result.returncode != 0:
        return {"error": f"Failed to retrieve service info: {show_result.stderr.strip()}"}

    # Parse key-value pairs from show
    show_info = {}
    for line in show_result.stdout.strip().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            show_info[key] = value

    # Run `systemctl status`
    status_result = run_systemctl_command("status", service)
    
    # Extract logs and info from status output regardless of return code
    # systemctl status returns 3 for inactive services, which is normal
    status_text = status_result.stdout
    timestamp_match = re.search(r"since\s+(.*?);", status_text) if status_text else None
    logs = status_text.strip().splitlines()[-5:] if status_text else []

    # Construct the response
    response = {
        "name": show_info.get("Id", service),
        "description": show_info.get("Description", "Unknown"),
        "active_state": show_info.get("ActiveState", "unknown"),
        "sub_state": show_info.get("SubState", "unknown"),
        "since": timestamp_match.group(1).strip() if timestamp_match else None,
        "main_pid": show_info.get("ExecMainPID", "N/A"),
        "start_command": show_info.get("ExecStart", "").split("argv[]=")[-1].split(";")[0].strip() if "ExecStart" in show_info else "",
        "logs": logs,
    }

    # Add error information only for non-standard errors
    if status_result.returncode != 0 and status_result.returncode != 3:
        response["error"] = f"Warning: Status command returned non-standard exit code {status_result.returncode}"

    return response
