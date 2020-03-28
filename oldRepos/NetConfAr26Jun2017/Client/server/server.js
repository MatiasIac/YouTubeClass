let express = require('express');
let app = express();
let server = require('http').createServer(app);
let socket = require('socket.io')(server);
let port = process.env.PORT || 8080;
let socketClients = [];
let players = [];

server.listen(port, function () {
    console.log(`Server listening at port ${port}`);
});

app.use(express.static(__dirname + '/../build'));

app.get('/api/move/:direction/:uid', function(req, res) {
    socketClients.forEach(function(item) {
        item.emit('move', { direction: req.params.direction, id: req.params.uid });
    });

    res.send('Moving');
});

app.get('/api/join/:uid', function(req, res) {
    socketClients.forEach(function(item) {
        item.emit('create', req.params.uid);
    });

    players.push(req.params.uid);
    res.send(req.params.uid);
});

socket.on("connect", function (client) {
    console.log("New Connection! " + client.client.id);
    socketClients.push(client);
    
    players.forEach(function(id) {
        client.emit('create', id);
    });
});