var Blynk = require('blynk-library');
var Gpio = require('onoff').Gpio;
var led = new Gpio(4,'out');

var AUTH = 'c34930742a774a788948f67ee289efe4';
var blynk = new Blynk.Blynk(AUTH);
var v0 = new blynk.VirtualPin(0);
v0.on('write'), function(param){
	if (param[0] == '1'){
		led.writeSync(1);
	}else{
		led.writeSync(0);
	}
	console.log('V0:', param[0]);
});