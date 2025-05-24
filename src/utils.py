import subprocess
import logging

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
    """Check the status of the specified server."""
    service = get_service_name(server_name)
    return run_systemctl_command("status", service)