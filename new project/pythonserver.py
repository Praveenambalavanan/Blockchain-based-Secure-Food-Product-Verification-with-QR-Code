import serial
import time
from flask import Flask, request

app = Flask(__name__)

# Change COM5 to your port (Linux = /dev/ttyUSB0)
ser = serial.Serial('COM5', 115200, timeout=1)
time.sleep(2)

@app.route('/get_object')
def get_object():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if "Detected:" in line:
            obj = line.split(":")[1].strip()
            return {"object": obj}
    return {"object": ""}

if __name__ == '__main__':
    app.run(port=5000)
