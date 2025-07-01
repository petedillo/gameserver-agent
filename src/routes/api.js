const express = require('express');
const router = express.Router({ mergeParams: true });
const palworldRouter = express.Router();

// Middleware to handle async routes
const asyncHandler = fn => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

/**
 * @swagger
 * /api/palworld/status:
 *   get:
 *     summary: Get server status and uptime
 *     tags: [Palworld]
 *     responses:
 *       200:
 *         description: Server status information
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   description: Current server status
 *                 uptime:
 *                   type: string
 *                   description: Server uptime
 */
palworldRouter.get('/status', asyncHandler(async (req, res) => {
  const status = await req.palworldService.getStatus();
  res.json(status);
}));

/**
 * @swagger
 * /api/palworld/start:
 *   post:
 *     summary: Start the Palworld server
 *     tags: [Palworld]
 *     responses:
 *       200:
 *         description: Server start command issued successfully
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 message:
 *                   type: string
 *                   example: Server start command issued successfully.
 */
palworldRouter.post('/start', asyncHandler(async (req, res) => {
  await req.palworldService.start();
  res.json({ message: 'Server start command issued successfully.' });
}));

/**
 * @swagger
 * /api/palworld/stop:
 *   post:
 *     summary: Stop the Palworld server
 *     tags: [Palworld]
 *     responses:
 *       200:
 *         description: Server stop command issued successfully
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 message:
 *                   type: string
 *                   example: Server stop command issued successfully.
 */
palworldRouter.post('/stop', asyncHandler(async (req, res) => {
  await req.palworldService.stop();
  res.json({ message: 'Server stop command issued successfully.' });
}));

/**
 * @swagger
 * /api/palworld/restart:
 *   post:
 *     summary: Restart the Palworld server
 *     tags: [Palworld]
 *     responses:
 *       200:
 *         description: Server restart command issued successfully
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 message:
 *                   type: string
 *                   example: Server restart command issued successfully.
 */
palworldRouter.post('/restart', asyncHandler(async (req, res) => {
  await req.palworldService.restart();
  res.json({ message: 'Server restart command issued successfully.' });
}));

/**
 * @swagger
 * /api/palworld/metrics:
 *   get:
 *     summary: Get server performance metrics
 *     tags: [Palworld]
 *     responses:
 *       200:
 *         description: Server performance metrics
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 cpuUsage:
 *                   type: number
 *                   description: Current CPU usage percentage
 *                 memoryUsage:
 *                   type: object
 *                   properties:
 *                     total:
 *                       type: number
 *                       description: Total memory in MB
 *                     used:
 *                       type: number
 *                       description: Used memory in MB
 *                     free:
 *                       type: number
 *                       description: Free memory in MB
 */
palworldRouter.get('/metrics', asyncHandler(async (req, res) => {
  const metrics = await req.palworldService.getMetrics();
  res.json(metrics);
}));

// Mount the palworld router under /palworld path
router.use('/palworld', palworldRouter);

module.exports = router;
