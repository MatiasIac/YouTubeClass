import pyfirmata2

DELAY = 1
PORT =  pyfirmata2.Arduino.AUTODETECT

board = pyfirmata2.Arduino(PORT)
board.samplingOn(100)
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()

while True:
    print(board.analog[0].read(), board.analog[1].read())
    board.pass_time(DELAY)