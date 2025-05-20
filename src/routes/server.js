const express = require('express');
const { exec } = require('child_process');
const router = express.Router();

const execPromise = (cmd) => {
    return new Promise((resolve, reject) => {
        // Execute commands on the host system via SSH
        const sshCmd = `ssh localhost '${cmd}'`;
        exec(sshCmd, (error, stdout, stderr) => {
            if (error) {
                reject({ success: false, message: error.message });
                return;
            }
            resolve({ success: true, message: stdout.trim() });
        });
    });
};

// Dashboard route
router.get('/', async (req, res) => {
    try {
        const status = await execPromise('systemctl is-active palserver');
        const logs = await execPromise('journalctl -u palserver --no-pager -n 10');
        res.render('dashboard', { 
            serverStatus: status.message,
            logs: logs.message.split('\n')
        });
    } catch (error) {
        res.render('dashboard', { 
            serverStatus: 'unknown', 
            error: error.message,
            logs: []
        });
    }
});

// Get server status
router.get('/server/status', async (req, res) => {
    try {
        const result = await execPromise('systemctl --user is-active palserver');
        res.json({ status: result.message });
    } catch (error) {
        res.json({ status: 'unknown', error: error.message });
    }
});

// Get server logs
router.get('/server/logs', async (req, res) => {
    try {
        const lines = req.query.lines || 10;
        const result = await execPromise(`journalctl -u palserver --no-pager -n ${lines}`);
        res.json({ success: true, logs: result.message.split('\n') });
    } catch (error) {
        res.json({ success: false, message: error.message });
    }
});

// Start server
router.post('/server/start', async (req, res) => {
    try {
        await execPromise('systemctl start palserver');
        res.json({ success: true, message: 'Server started successfully' });
    } catch (error) {
        res.json({ success: false, message: error.message });
    }
});

// Restart server
router.post('/server/restart', async (req, res) => {
    try {
        await execPromise('systemctl restart palserver');
        res.json({ success: true, message: 'Server restarted successfully' });
    } catch (error) {
        res.json({ success: false, message: error.message });
    }
});

// Stop server
router.post('/server/stop', async (req, res) => {
    try {
        await execPromise('systemctl stop palserver');
        res.json({ success: true, message: 'Server stopped successfully' });
    } catch (error) {
        res.json({ success: false, message: error.message });
    }
});

module.exports = router;
