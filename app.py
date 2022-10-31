'''
Created 27 October 2022
'''

from flask import Flask, render_template, Response
import camera

app = Flask(__name__)
cam = camera.Camera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(cam.stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)


