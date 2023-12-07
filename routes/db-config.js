// Define constants for shorthand use elsewhere

const sql = require("mysql");
const db = sql.createConnection({
  host: process.env.DATABASE_HOST,
  user: process.env.DATABASE_USER,
  password: process.env.DATABASE_PASSWORD,
  database: process.env.DATABASE,
});

// Export the database connection to anywhere it is needed throughout the project

module.exports = db;
