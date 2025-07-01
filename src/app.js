require('dotenv').config();
const fs = require('fs');
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const swaggerJsdoc = require('swagger-jsdoc');
const apiRoutes = require('./routes/api');
const SSHService = require('./services/sshService');
const PalworldService = require('./services/palworld');

const app = express();
const port = process.env.PORT || 3000;

// CORS configuration
const allowedOrigins = [
  'https://gameserver.petedillo.com',
  'http://localhost:3000',
  'http://127.0.0.1:3000'
];

const corsOptions = {
  origin: (origin, callback) => {
    if (!origin || allowedOrigins.indexOf(origin) !== -1) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,
  optionsSuccessStatus: 200
};

app.use(cors(corsOptions));

// Swagger definition
const swaggerOptions = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'GameServer Agent API',
      version: '1.0.0',
      description: 'An API to manage a Palworld game server.',
    },
    servers: [
      {
        url: '/',
        description: 'Current server',
      },
      {
        url: 'https://api.gameserver.petedillo.com',
        description: 'Production server',
      },
      {
        url: `http://localhost:${port}`,
        description: 'Local development',
      },
    ],
  },
  apis: ['./src/routes/*.js'],
  explorer: true,
};

const swaggerSpec = swaggerJsdoc(swaggerOptions);
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

// SSH and Palworld Service Initialization
const sshConfig = {
  SSH_HOST: process.env.SSH_HOST,
  SSH_PORT: process.env.SSH_PORT,
  SSH_USER: process.env.SSH_USER,
  SSH_PRIVATE_KEY: fs.readFileSync(process.env.SSH_PRIVATE_KEY_PATH, 'utf8'),
};

const sshService = new SSHService(sshConfig);
const palworldService = new PalworldService(sshService);

// Middleware to attach services to request
app.use((req, res, next) => {
  req.palworldService = palworldService;
  next();
});

// API Routes
app.use('/api', apiRoutes);

// Global error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: err.message || 'Something went wrong!' });
});

const startServer = async () => {
  try {
    console.log('Connecting to SSH server...');
    await sshService.connect();
    console.log('SSH connection successful.');

    app.listen(port, () => {
      console.log(`Server is running on http://localhost:${port}`);
      console.log(`API documentation available at http://localhost:${port}/api-docs`);
    });
  } catch (error) {
    console.error('Failed to connect to SSH server:', error);
    process.exit(1);
  }
};

startServer();

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('Shutting down...');
  sshService.disconnect();
  process.exit(0);
});
