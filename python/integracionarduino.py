import serial
import simplejson

ser = serial.Serial('COM3', 115200)

while True:
    jsonResult = ser.readline()

    try:
        jsonObject = simplejson.loads(jsonResult)
        print jsonObject["x"]
    except Exception:
        pass
