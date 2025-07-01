const express = require('express');
const router = express.Router();

// Middleware to handle async routes
const asyncHandler = fn => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// GET /status - Get server status and uptime
router.get('/status', asyncHandler(async (req, res) => {
  const status = await req.palworldService.getStatus();
  res.json(status);
}));

// POST /start - Start the server
router.post('/start', asyncHandler(async (req, res) => {
  await req.palworldService.start();
  res.json({ message: 'Server start command issued successfully.' });
}));

// POST /stop - Stop the server
router.post('/stop', asyncHandler(async (req, res) => {
  await req.palworldService.stop();
  res.json({ message: 'Server stop command issued successfully.' });
}));

// POST /restart - Restart the server
router.post('/restart', asyncHandler(async (req, res) => {
  await req.palworldService.restart();
  res.json({ message: 'Server restart command issued successfully.' });
}));

// GET /metrics - Get performance metrics
router.get('/metrics', asyncHandler(async (req, res) => {
  const metrics = await req.palworldService.getMetrics();
  res.json(metrics);
}));

module.exports = router;
