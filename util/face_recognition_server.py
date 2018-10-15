from flask import Flask, request
from util.face_service import get_contrast_faces_result
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()
app = Flask(__name__)


@app.route('/contrast_faces', methods=['POST'])
def contrast_faces_result():
    params = request.json
    known_image_code = params["known_image_code"]
    unknown_image_code = params["unknown_image_code"]

    return get_contrast_faces_result(known_image_code, unknown_image_code)


if __name__ == "__main__":
    http_server = WSGIServer(('192.168.131.146', 8080), app)
    http_server.serve_forever()
