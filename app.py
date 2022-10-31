'''
Created 27 October 2022
'''

from urllib import response
from flask import Flask, render_template, Response, jsonify
import camera
import wet_floor_sign

app = Flask(__name__)
cam = camera.Camera()
ml = wet_floor_sign.WetFloorSign()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(cam.stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/classify_feed')
def classify_feed():
    response = ml.classify(cam.getPhoto(), cam.get_current_cam())
    return jsonify(response)




if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)


