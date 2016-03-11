var express = require('express');
var Twitter = require('twitter');
var fs = require('fs');
var path = require('path');

var app = express();
app.use(express.static('public'));
//app.use(express.static('bower_components'));

var client = new Twitter({
	consumer_key: 'Nd5GKMznzMpEvZswS4Dauh63Q',
	consumer_secret: 'mqDrczSwkHn17xgHq9n18YkkI2t1WMq7lgDW7YdE10oL4fPcgP',
	access_token_key: '263805779-UARQgvNfsiNX8QXsBU5jJf3TiqlWPSRpHPPHIyQO',
	access_token_secret: 'lrje1MJohMRInwmCSbY9rxFTX73VMQQN7mrCmdzVcWKID'
});
var result;

app.get('/completeness', function(req, res){

	var params = {"count": '200'};
	client.get('statuses/home_timeline', params, function (error, tweets, response){
		if (!error){
			result = tweets;
		}
	});
	
	//res.send('hello express');
	res.sendfile(path.join(__dirname, '/public/prueba.html'));
});

app.post('/data', function(req, res) {
	console.log(req);
});

app.listen(8080, function() {
	console.log("Servidor up!");
});


String.prototype.to_rfc3986 = function (){
   var tmp =  encodeURIComponent(this);
   tmp = tmp.replace('!','%21');
   tmp = tmp.replace('*','%2A');
   tmp = tmp.replace('(','%28');
   tmp = tmp.replace(')','%29');
   tmp = tmp.replace("'",'%27');
   return tmp;
};

//var test_key = 'xvz1evFS4wEEPTGEFPHBog';
//var test_secret = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg';

// const options = {
// 	key: fs.readFileSync('../../key.pem'),
// 	cert: fs.readFileSync('../../key-cert.pem')
// }

// var prepareData = function(consumer_key, consumer_secret){
// 	/* Encode the values of consumer key and secret according to RFC 1738 --> 3986 */
// 	consumer_key = consumer_key.to_rfc3986();
// 	consumer_secret = consumer_secret.to_rfc3986();
// 	// Parameter to the POST request
// 	var auth = consumer_key + ":" + consumer_secret;
// 	auth = new Buffer(auth).toString('base64');
// 	return auth;
// }

// var handler = function(resp, res){
// 	//res.writeHead('200');
// 	//console.log("The token is ready");
// 	resp = JSON.parse(resp);
// 	console.log(resp.access_token);
// 	var option = {
// 		host: 'api.twitter.com',
// 		path: '/1.1/statuses/user_timeline.json?screen_name=twitterTimeline&count=200',
// 		method: 'GET',
// 		headers: {
// 			'Authorization': 'Bearer ' + resp.access_token
// 			//'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
// 		}
// 	}
// 	var t = [];
// 	var pet = https.request(option, function(response){
// 		response.on('data', function(chunk){
// 			var item = chunk;
// 			t.push(JSON.parse(item));
// 		})
// 		.on('end', function(){
// 			res.writeHead('200');
// 			res.end("The response has been received" + JSON.stringify(t));
// 		})
// 		.on('error', function(msg){
// 			console.log(msg);
// 		});
// 	});

// 	pet.end();
// }

// var server = https.createServer(options, function(req, res) {

// 	var auth = prepareData(consumer_key, consumer_secret);
// 	/* Let's enable the parameters for make the login POST request */
// 	var postData = querystring.stringify({
//   		'grant_type' : 'client_credentials'
// 	});
// 	var opt = {
// 		host: 'api.twitter.com',
// 		path: '/oauth2/token',
// 		method: 'POST',
// 		headers: {
// 			'Authorization': 'Basic ' + auth,
// 			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
// 		}
// 	};
// 	var resp;
// 	var request = https.request(opt, function(response){
// 		response.on('error', function(msg){
// 			console.log(msg);
// 		}).on('data', function(chunk){
// 			resp = chunk;
// 		})
// 		.on('end', function(){
// 			handler(resp, res);
// 		});
// 	});

// 	request.write(postData);
// 	request.end();
	
// });

// server.listen(8080);
