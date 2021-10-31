const express = require("express");
const path = require("path");
const router = express.Router();

router.get('/', function(req, res){
    res.render(path.join(__dirname, "templates/home.ejs"))
});

module.exports = router;
