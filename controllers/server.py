import logging
import mimetypes
import cv2

from flask import request
from flask import jsonify
from requests import Response

import config


from droneapp.models.drone_manager import DroneManager
from flask import render_template

logger = logging.getLogger(__name__)
app = config.app

def get_drone():
    return DroneManager()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/controller/')
def controller():
    return render_template('controller.html')

@app.route('/video_feed/')
def video_feed():
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route('/api/command/', methods = ['POST'])
def command():
    cmd = request.form.get('command')
    logger.info({'action':'command', 'cmd': cmd})
    drone = get_drone()
    
    if cmd == 'takeOff':
        drone.takeoff()
    if cmd == 'land':
        drone.land()
    if cmd == 'speed':
        speed = request.form.get('speed')
        logger.info({'action': 'command', 'cmd': cmd, 'speed' : speed})
        if speed:
            drone.set_speed(int(speed))
    
    if cmd == 'up':
        drone.up()
    if cmd == 'down':
        drone.down()
    if cmd == 'forward':
        drone.forward()
    if cmd == 'back':
        drone.back()
    if cmd == 'clockwise':
        drone.clockwise()
    if cmd == 'counterClockwise':
        drone.counter_clockwise()
    if cmd == 'left':
        drone.left()
    if cmd == 'right':
        drone.right()
    if cmd == 'flipFront':
        drone.flip_front()
    if cmd == 'flipBack':
        drone.flip_back()
    if cmd == 'flipRight':
        drone.flip_right()
    if cmd == 'flipLeft':
        drone.flip_left()








    return jsonify(status = 'success'), 200


def run():
    app.run(host=config.WEB_ADDRESS, port=config.WEB_PORT, threaded = True)
    #remove threaded

def generate():
    cam = cv2.VideoCapture(0)
    while True:
        frame = cam.read()
        (flag ,encodedImage) = cv2.imencode(".jpg",frame.copy())
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'+ bytearray(encodedImage) +b'\r\n')
