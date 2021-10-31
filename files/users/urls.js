const express = require("express");
const path = require("path");
const router = express.Router();

router.get('/sign-in', function(req, res){
    res.render(path.join(__dirname, "templates/sign-in"))
});

module.exports = router;
