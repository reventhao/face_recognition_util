from flask import Flask, request
from FaceUtil import contrast_faces, convert_to_image
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()
app = Flask(__name__)

DECODING_ERROR = "001"              # 转换编码为图片错误
FACE_NOT_FOUND = "002"              # 没有找到人脸错误
COMPARE_ERROR = "003"               # 人脸比对错误
SAME_PERSON = "yes"                 # 同一个人
NOT_SAME_PERSON = "no"              # 不是同一个人


@app.route('/contrast_faces', methods=['POST'])
def contrast_faces_result():
    params = request.json
    known_image_code = params["known_image_code"]
    unknown_image_code = params["unknown_image_code"]
    known_image = convert_to_image(known_image_code)
    unknown_image = convert_to_image(unknown_image_code)
    if isinstance(known_image, str) or isinstance(unknown_image, str):
        result = DECODING_ERROR
    else:
        result = contrast_faces(known_image, unknown_image)
        if result == "nf":
            result = FACE_NOT_FOUND
        elif result == "err":
            result = COMPARE_ERROR
        elif result:
            result = SAME_PERSON
        else:
            result = NOT_SAME_PERSON
    return result


if __name__ == "__main__":
    http_server = WSGIServer(('192.168.131.146', 8080), app)
    http_server.serve_forever()
