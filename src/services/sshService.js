const { Client } = require('ssh2');

class SSHService {
  constructor(config) {
    this.ssh = new Client();
    this.config = config;
  }

  connect() {
    return new Promise((resolve, reject) => {
      this.ssh.on('ready', () => {
        resolve();
      }).on('error', (err) => {
        reject(err);
      }).connect({
        host: this.config.SSH_HOST,
        port: this.config.SSH_PORT || 22,
        username: this.config.SSH_USER,
        privateKey: this.config.SSH_PRIVATE_KEY
      });
    });
  }

  async executeCommand(command) {
    return new Promise((resolve, reject) => {
      this.ssh.exec(command, (err, stream) => {
        if (err) return reject(err);
        let stdout = '';
        let stderr = '';
        stream.on('close', (code) => {
          if (code !== 0) {
            return reject(new Error(`Command failed with exit code ${code}: ${stderr}`));
          }
          resolve({ stdout, stderr });
        }).on('data', (data) => {
          stdout += data.toString();
        }).stderr.on('data', (data) => {
          stderr += data.toString();
        });
      });
    });
  }

  disconnect() {
    this.ssh.end();
  }
}

module.exports = SSHService;
