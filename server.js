if(process.env.NODE_ENV !== 'production') {
  require('dotenv').config()
}

// Set up constants to reduce code length

const express = require('express');
const app = express();
const expressLayouts = require('express-ejs-layouts');
const indexRouter = require('./routes/index');
const mongoose = require('mongoose');
const db = mongoose.connection;

// Set the resources the application will use

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');
app.set('layout', 'layouts/layout');
app.use(expressLayouts);
app.use(express.static('public'));
app.use('/', indexRouter);

// Set the port that the server will operate on by default

app.listen(process.env.PORT || 3000);

// Connect to MongoDB

mongoose.connect(process.env.DATABASE_URL);
db.on('error', error => console.error(error));
db.once('open', ()=> console.log('Connected to Mongoose!'));