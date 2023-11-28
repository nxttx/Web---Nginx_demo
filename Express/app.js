/**
 * Express webapi framework
 */
import express from 'express';
import bodyParser from "body-parser";

const app = express();


// middleware
app.use(bodyParser.json()); // makes req.body available

// helloworld
app.get('/', function(req, res, next) {
  res.send('Hello World! From nodejs');
});

// return 1
app.get('/check', function(req, res, next) {
  res.send('1');
});




// start server
app.listen(80);