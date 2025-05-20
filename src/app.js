const express = require('express');
const path = require('path');
const serverRoutes = require('./routes/server');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

// Configure Twig
app.set('view engine', 'twig');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

// Routes
app.use('/', serverRoutes);

app.listen(port, () => {
    console.log(`PalWorld Server Manager running on http://localhost:${port}`);
});
