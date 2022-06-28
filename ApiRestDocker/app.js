const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const { dbConnection } = require('./db/config');
const path = require('path');
require('dotenv').config();

// Create the express server 
const app = express();

// We start the Database
dbConnection();

// Read every request and response and display it on the console
app.use(morgan('dev'));

// Public Directory
app.use(express.static('public'));
app.use('/uploads', express.static(path.resolve('uploads')));

// Use CORS
app.use(cors());


// Reading and parsing the body, Indicates that the incoming data is Json
app.use(express.json({ limit: '50mb'}));
app.use(express.urlencoded({ limit:'50mb' }))
// Routes
app.use('/api/files', require('./routes/files.router'));

// Handle other angular routes
app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'public/index.html'));
})

module.exports = app;