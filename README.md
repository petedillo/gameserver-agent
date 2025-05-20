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

4. Set up sudo permissions:
   ```bash
   sudo cp sudoers-palworld /etc/sudoers.d/palworld
   sudo chmod 440 /etc/sudoers.d/palworld
   ```

5. Install and start the service:
   ```bash
   sudo cp palworld-manager.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable palworld-manager
   sudo systemctl start palworld-manager
   ```

## Development

Run the application in development mode:
```bash
npm run dev
```

For production:
```bash
npm start
```
