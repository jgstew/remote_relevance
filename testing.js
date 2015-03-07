
// http://stackoverflow.com/questions/5869216/how-to-store-node-js-deployment-settings-configuration-files
var config = require('./config.json');

var rest_api_url = "https://" + config.bigfix_server_host + ":" + config.bigfix_server_port + "/api/";

console.log('-------------');
console.log('-- testing --');
console.log( rest_api_url );
