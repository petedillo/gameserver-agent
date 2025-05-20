# PalWorld Server Manager

A Node.js Express-based web service for managing a PalWorld dedicated server through systemd. This application provides a web interface to monitor and control your PalWorld dedicated server.

## Features

- 🎮 Real-time server status monitoring
- 🔄 Start/Stop/Restart server controls
- 📋 Server logs viewer with auto-refresh
- 🚀 Systemd service integration

## Prerequisites

- Node.js 16 or higher
- PalWorld dedicated server installed and configured as a systemd service
- Sudo access for systemctl commands

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/petedillo/palserver-api.git
   cd palserver-api
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables:
   ```bash
   cp src/.env.example src/.env
   # Edit src/.env with your preferred settings
   ```

4. Set up required permissions:
   - Ensure the user running the application has sudo access to the following commands:
     - systemctl start palserver
     - systemctl stop palserver
     - systemctl restart palserver
     - systemctl is-active palserver
     - journalctl -u palserver

5. Run the application:
   ```bash
   # Start the application
   npm start
   ```

   The server will be available at http://localhost:3000 (or your configured port)

## Docker

You can run this application using Docker:

```bash
# Build the image
docker build -t diolab:5000/palserver-api:latest .

# Run the container
docker run -d \
  --name palserver-manager \
  -p 3000:3000 \
  --restart unless-stopped \
  diolab:5000/palserver-api:latest

# Push to registry
docker push diolab:5000/palserver-api:latest
```

Note: When running in Docker, ensure the container has the necessary permissions to execute systemctl commands on the host system.

## Development

Run the application in development mode:
```bash
npm run dev
```

For production:
```bash
npm start
```
