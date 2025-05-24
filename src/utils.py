import subprocess

def get_service_name(server_name):
    """Get the appropriate service name based on the server type."""
    if server_name == "palworld":
        return "palworld.service"
    return f"docker-compose@{server_name}.service"

def start_server(server_name):
    """Start the specified server."""
    service = get_service_name(server_name)
    command = f"sudo systemctl start {service}"
    return subprocess.run(command, shell=True, capture_output=True)

def stop_server(server_name):
    """Stop the specified server."""
    service = get_service_name(server_name)
    command = f"sudo systemctl stop {service}"
    return subprocess.run(command, shell=True, capture_output=True)

def restart_server(server_name):
    """Restart the specified server."""
    service = get_service_name(server_name)
    command = f"sudo systemctl restart {service}"
    return subprocess.run(command, shell=True, capture_output=True)

def check_status(server_name):
    """Check the status of the specified server."""
    service = get_service_name(server_name)
    command = f"sudo systemctl status {service}"
    return subprocess.run(command, shell=True, capture_output=True)