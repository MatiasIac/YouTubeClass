const five = require("johnny-five");
const board = new five.Board();

board.on("ready", function() {

    const joystick = new five.Joystick({
        pins: ["A0", "A1"]
    });

    joystick.on("change", function () {
        console.log(this.x);
    });

});