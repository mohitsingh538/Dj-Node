const express = require("express");
const path = require("path");
const router = express.Router();
const fs = require('fs');

router.get('/', function(req, res){
    var pkg_file = fs.readFileSync('package.json');
    var proj_name = JSON.parse(pkg_file);
    res.render(path.join(__dirname, "templates/home.ejs"), {projName: proj_name.name})
});

module.exports = router;
