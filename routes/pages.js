const express = require("express");
const router = express.Router();

// Set the root URL to the index.ejs landing page

router.get("/", (req, res) => {
  res.render("index");
});

// Export the router function

module.exports = router;
