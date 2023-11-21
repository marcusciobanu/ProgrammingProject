// Define constants for ease of use

const express = require('express');
const db = require('./routes/db-config');
const app = express();
const cookie = require('cookie-parser');
const cookieParser = require('cookie-parser');
const PORT = process.env.PORT || 3000;

// Key settings for the app

app.use(express.static(__dirname + '/public'));
app.set('view engine', 'ejs');
app.set('views', './views');
app.use(cookie());
app.use(express.json());

// Selects the port that the server listens to as set previously

app.listen(PORT);

// Connect to database

db.connect((err) => {
  if(err) throw err;
  console.log('database connected');
})

// Set the routing module

app.use('/', require('./routes/pages'));
