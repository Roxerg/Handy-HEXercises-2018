

var ws = new WebSocket("ws://localhost:8000/")
var jsondata = "{}"


ws.onmessage = function (event) {
    // to test whether connection is working
    console.log(event.data);
  }

ws.onopen = function (event) {
    ws.send(jsondata)
}

sendspam = function() {
    ws.send(Math.floor((Math.random() * 10) + 1));
}

setTimeout(function() {
    sendspam();
}, 2000);

// ws.send(json) that's all you need to pass data bitch