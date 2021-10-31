const express = require("express");
const app = express();
const path = require("path");
require('dotenv').config()
const env_vars = process.env;


app.set('port', env_vars.API_PORT);
app.set("view engine", "ejs");
app.set('views', path.join(__dirname, 'templates'));
app.use(express.static(path.join(__dirname, "static")));



for(var iter = 0; iter < settings.config.INSTALLED_APPS.length; iter++){
  var route = `./${settings.config.INSTALLED_APPS[iter]}/urls`;
  var routes = require(route);
  app.use(routes);
}











// Handle 404
app.use(function(req, res) {
  res.status(400);
  res.render('404.ejs');
});


app.listen(env_vars.API_PORT, () => {
  console.log(`Development server started at http://127.0.0.1:${env_vars.API_PORT}`);
});

module.exports = app;
