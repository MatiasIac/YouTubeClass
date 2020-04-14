import pyfirmata2

DELAY = 1
PORT = pyfirmata2.Arduino.AUTODETECT

board = pyfirmata2.Arduino(PORT)

while True:
    board.digital[13].write(1)
    board.pass_time(DELAY)
    board.digital[13].write(0)
    board.pass_time(DELAY)