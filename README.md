# GameServer Agent for Palworld

This project provides a Dockerized Express.js API to manage a Palworld dedicated server over SSH. It allows for starting, stopping, restarting, and monitoring the server status.

## Features

- **Remote Control:** Start, stop, and restart the Palworld server using API endpoints.
- **Status Monitoring:** Check the server's real-time status (`active`, `inactive`) and uptime.
- **Containerized:** Runs in a Docker container for easy deployment and isolation.
- **API Documentation:** Includes Swagger UI for interactive API documentation.

## Technical Stack

- **Runtime:** Node.js 18+
- **Web Framework:** Express.js
- **SSH Client:** `ssh2` library
- **Containerization:** Docker & Docker Compose
- **Configuration:** Environment variables (`.env` file)
- **Documentation:** OpenAPI (Swagger)

## Prerequisites

- Docker and Docker Compose installed on your local machine.
- A running Palworld dedicated server on a remote machine, managed by `systemd`.
- SSH access to the remote server with key-based authentication.

## Setup and Deployment

### 1. Configure the Remote Server

On your Palworld game server, you need to ensure the following:

- The Palworld server is set up as a `systemd` service (e.g., `palworld-dedicated.service`).
- The SSH user (`SSH_USER`) has passwordless `sudo` permissions to manage this specific service with `systemctl`. You can add the following line to your sudoers file using `sudo visudo`:

  ```
  your_ssh_user ALL=(ALL) NOPASSWD: /usr/bin/systemctl start palworld-dedicated, /usr/bin/systemctl stop palworld-dedicated, /usr/bin/systemctl restart palworld-dedicated
  ```

- The SSH user's public key is added to the `~/.ssh/authorized_keys` file.

### 2. Configure the Agent

1.  **Clone the repository (if applicable) or use the generated code.**

2.  **Create an environment file:**
    Copy the `.env.example` to a new file named `.env`.

    ```bash
    cp .env.example .env
    ```

3.  **Update the `.env` file** with your remote server's details:

    ```ini
    # Server Configuration
    PORT=3000

    # SSH Connection Settings
    SSH_HOST=your_server_ip
    SSH_USER=your_ssh_user
    SSH_PORT=22

    # Path to the SSH private key inside the container
    SSH_PRIVATE_KEY_PATH=/app/ssh/gameserver_agent
    ```

4.  **Add the SSH Private Key:**
    Place your SSH private key file in the `ssh/` directory. The filename must match the `SSH_PRIVATE_KEY_PATH` value in your `.env` file (e.g., `ssh/gameserver_agent`).

### 3. Build and Run the Container

Once the configuration is complete, you can build and run the agent using Docker Compose:

```bash
# Build the Docker image
docker-compose build

# Start the container in detached mode
docker-compose up -d
```

The agent will now be running and accessible on the port you specified (default: 3000).

## API Documentation

Interactive API documentation is available via Swagger UI. Once the agent is running, you can access it at:

[http://localhost:3000/api-docs](http://localhost:3000/api-docs)

### API Endpoints

- `GET /api/status`: Get the current server status (`active`/`inactive`) and uptime.
- `POST /api/start`: Start the Palworld server.
- `POST /api/stop`: Stop the Palworld server.
- `POST /api/restart`: Restart the Palworld server.
- `GET /api/metrics`: Get performance metrics (placeholder, not fully implemented).

## Security Best Practices

- **Firewall:** Ensure that only trusted IP addresses can access the agent's API port.
- **SSH Key Security:** The private key used by the agent should be unique and have the minimum required permissions. Do not expose this key publicly.
- **Principle of Least Privilege:** The SSH user on the game server should only have permissions to manage the Palworld service and nothing more.
- **No Authentication:** This agent does not have an authentication layer by design. It is meant to be run in a trusted, internal network. Do not expose it directly to the internet without a reverse proxy or API gateway that can handle authentication and TLS termination.
