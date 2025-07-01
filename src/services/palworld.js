class PalworldService {
  constructor(sshService) {
    this.ssh = sshService;
    // Use environment variable for service name, default to 'palworld' if not set
    this.SERVICE_NAME = process.env.PALWORLD_SERVICE_NAME || 'palworld';
  }

  async getStatus() {
    try {
      const { stdout } = await this.ssh.executeCommand(`systemctl is-active ${this.SERVICE_NAME}`);
      const status = stdout.trim();
      let uptime = null;

      if (status === 'active') {
        uptime = await this.getUptime();
      }

      return {
        status,
        uptime
      };
    } catch (error) {
        // If command fails, it's likely because the service is not running
        if (error.message.includes('exit code')) {
            return { status: 'inactive', uptime: null };
        }
        throw error;
    }
  }

  async start() {
    return this.ssh.executeCommand(`sudo systemctl start ${this.SERVICE_NAME}`);
  }

  async stop() {
    return this.ssh.executeCommand(`sudo systemctl stop ${this.SERVICE_NAME}`);
  }

  async restart() {
    return this.ssh.executeCommand(`sudo systemctl restart ${this.SERVICE_NAME}`);
  }

  async getUptime() {
    const { stdout } = await this.ssh.executeCommand(
      `systemctl show -p ActiveEnterTimestamp ${this.SERVICE_NAME} | cut -d= -f2-`
    );
    return stdout.trim();
  }

  async getMetrics() {
    // Placeholder for metrics logic
    return { message: 'Metrics not implemented yet.' };
  }
}

module.exports = PalworldService;
