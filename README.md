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
- User permissions to run systemctl commands for the palserver service

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

3. Configure system permissions:
   Create a new sudoers file for the application:
   ```bash
   sudo visudo -f /etc/sudoers.d/palserver
   ```

   Add the following to the sudoers file (replace `youruser` with your username):
   ```
   youruser ALL=(ALL) NOPASSWD: /bin/systemctl start palserver
   youruser ALL=(ALL) NOPASSWD: /bin/systemctl stop palserver
   youruser ALL=(ALL) NOPASSWD: /bin/systemctl restart palserver
   youruser ALL=(ALL) NOPASSWD: /bin/systemctl is-active palserver
   youruser ALL=(ALL) NOPASSWD: /bin/journalctl -u palserver
   ```

4. Configure environment variables:
   ```bash
   cp src/.env.example src/.env
   # Edit src/.env if you want to change the port (default: 3000)
   ```

5. Run the application:
   ```bash
   # Start the application
   npm start
   ```

   The server will be available at http://localhost:3000 (or your configured port)

## Development

Run the application in development mode:
```bash
npm run dev
```

For production:
```bash
npm start
```

## Security Considerations

- Run the application as a non-root user
- Keep sudo permissions limited to only the required commands
- Consider implementing additional authentication for the web interface
- Monitor system logs for unauthorized access attempts
- Consider running behind a reverse proxy for HTTPS support
