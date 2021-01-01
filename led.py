
from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# {{url}}/led?status=on
@app.route('/', methods=['GET'])
def led():
    status = request.args.get('status')
    led = request.args.get('led')
    if status == "on":
        if led == "ledrelay1":
            GPIO.output(18, GPIO.HIGH)
        elif led == "ledrelay2":
            GPIO.output(23, GPIO.HIGH)
        else:
            return jsonify({"message":"led non reconnu"})
        return jsonify({"message": "Led allume avec succes"})
    elif status == "off":
        if led == "ledrelay1":
            GPIO.output(18, GPIO.LOW)
        elif led == "ledrelay2":
            GPIO.output(23, GPIO.LOW)
        else:
            return jsonify({"message": "Led non reconnu"})
        return jsonify({"message": "Led eteinte avec succes"})
    else:
        return jsonify({"message": "Status non valide"})

