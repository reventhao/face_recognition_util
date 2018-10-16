from flask import Flask, request
from util.face_service import get_contrast_faces_result
from gevent import monkey
from gevent.pywsgi import WSGIServer
import configparser

monkey.patch_all()
config = configparser.ConfigParser()
config.read("wsgi_config.conf")
IP = config['config']['ip']
PORT = int(config['config']['port'])
app = Flask(__name__)


@app.route('/contrast_faces', methods=['POST'])
def contrast_faces_result():
    params = request.json
    known_image_code = params["known_image_code"]
    unknown_image_code = params["unknown_image_code"]

    return get_contrast_faces_result(known_image_code, unknown_image_code)


if __name__ == "__main__":
    http_server = WSGIServer((IP, PORT), app)
    http_server.serve_forever()
