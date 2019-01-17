from flask import (Flask, render_template, request,
					redirect, url_for, make_response, Response)
import os
from camera_opencv import Camera
app = Flask(__name__)
a = None
@app.route('/', methods = ['GET','POST'])
def index():
	a, b, c = request.form.get('check1'), request.form.get('check2'), request.form.get('check3')
	print(a,b,c)
	return render_template("index.html")

def gen(camera):
    """Video streaming generator function."""
    while True:
        camera.getstat(a)
        print(a)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port = 8000)