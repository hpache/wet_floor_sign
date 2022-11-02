'''
Created 27 October 2022
'''


from flask import Flask, redirect, render_template, Response, jsonify, request, url_for
from tensorflow.python.framework.ops import re
from werkzeug.wrappers import response
import camera
import wet_floor_sign

app = Flask(__name__)
cam = camera.Camera()
ml = wet_floor_sign.WetFloorSign()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():

    if len(list(request.form)) > 0:
        numCams = int(request.args.get("numCams"))
        cam_urls = [request.args.get(str(i+1)) for i in range(numCams)]
        cam.setCameraUrls(cam_urls)
        cam.setNumberCameras(numCams)
    return redirect(url_for('guard'))

@app.route('/guard', methods=['GET', 'POST'])
def guard():
    return render_template('guard.html')

@app.route('/initialize')
def initialize():
    return jsonify({'num_cams':cam.getNumberCameras()})

@app.route('/video_feed')
def video_feed():
    return Response(cam.stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/classify_feed')
def classify_feed():
    response = ml.classify(cam.getPhoto(), cam.getCurrentCamera())
    return jsonify(response)


@app.route('/update', methods=['POST'])
def update():
    response_dict = request.get_json('ajax')
    return jsonify(ml.update(response_dict))



if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)


