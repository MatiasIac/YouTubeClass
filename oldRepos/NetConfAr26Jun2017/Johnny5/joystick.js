const endpoint_url = "http://localhost:8080/api/";
const uuid = require('uuid/v1');
let five = require("johnny-five");
let request = require("request");
let board = new five.Board();
let player_id = null;
let last_direction = 0;

board.on("ready", function() {

    let id = uuid();
    console.log(`device id: ${id}`);

    request(endpoint_url + "join/" + id, function (error, response, body) {
        player_id = response.body;
        console.log("joined to the game");
    });

    let joystick = new five.Joystick({
        pins: ["A0", "A1"]
    });

    joystick.on("change", function() {
        if (this.x > 0.9 || this.x < -0.9 || this.x < 0.2 || this.x > -0.2) {
            if (player_id !== null) {
                let direction = this.x > 0.9 ? 1 : this.x < -0.9 ? -1 : 0;

                if (last_direction !== direction) {
                    console.log(`data sent: ${direction}`);

                    request(endpoint_url + "move/" + direction + "/" + player_id, function (error, response, body) {
                    });

                    last_direction = direction;
                }
            }
        }
    });

    this.repl.inject({ joystick: joystick });
});