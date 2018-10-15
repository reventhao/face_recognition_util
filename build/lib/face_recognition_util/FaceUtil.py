import face_recognition
import numpy as np
import cv2
import base64
from PIL import Image, ImageDraw, ImageFont


class FaceNotFoundException(Exception):

    def __init__(self):
        err = "Compare Failure,cannot find face in image"
        Exception.__init__(self, err)


# base64转opencv图片
def convert_to_image(base64_code):
    """
    base64转换图片
    :参数 base64_code 需要转换为opencv图片格式的base64编码
    :返回值: 转换完成的opencv2格式图片
    """
    # base64解码
    b64image = base64.b64decode(base64_code)
    # 转opencv图片
    image_array = np.frombuffer(b64image, np.uint8)
    result_image = cv2.imdecode(image_array, cv2.COLOR_BGR2RGB)
    # 返回opencv图片对象
    if result_image is None:
        return "error"
    else:
        return result_image


# 缩放图片
def resize_image(image, multiple=1.0):
    """
    缩放图片加快识别
    :参数1 image 需要缩放的图片
    :参数2 fsize 缩放倍数,默认值为1，基准120大小等比缩放
    :返回值: 缩放完成的opencv2格式图片
    """
    # 默认以基准120大小等比例缩小
    base_height = 120
    image_height = image.shape[0]
    if multiple == 1:
        multiple = base_height / image_height
    result_image = cv2.resize(image, (0, 0), fx=multiple, fy=multiple)

    return result_image


# 获取单个人脸128特征点向量
def get_face_encoding(face_image):
    """
    获取图片中单个人脸128特征点向量
    :参数 face_image 需要获取特征点向量图片
    :返回值: 特征点向量
    """
    face_encoding = face_recognition.face_encodings(face_image)[0]
    return face_encoding


# 人脸比对
def contrast_faces(known_image, unknown_image):
    """
    人脸对比
    :参数1 known_image:已知人脸图片
    :参数2 unknown_image:未知人脸图片
    :返回值: 比对结果
    """
    # noinspection PyBroadException
    try:
        known_image_encoding = face_recognition.face_encodings(resize_image(known_image))[0]
        unknown_image_encoding = face_recognition.face_encodings(resize_image(unknown_image))[0]
        result = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding, 0.4)
        return result[0]
    except IndexError:
        return "nf"
    except Exception as e:
        print("recognition error！\n cause：{}".format(e))
        return "err"


# 摄像头实时比对
def real_time_comparison(known_face_encodings, known_face_names):
    """
    开启摄像头实时比对
    :参数1 known_face_encodings:已知多个人脸128特征点向量数组
    :参数2 known_face_names:已知多个人脸对应名称
    """
    process_this_frame = True
    face_locations = ""
    face_names = ""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        frame = cv2.flip(frame, 1, dst=None)

        small_frame = resize_image(frame, 0.5)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.4)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            cv2.rectangle(frame, (left - 10, top - 10), (right + 10, bottom + 10), (0, 0, 255), 1)
            cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 100), cv2.FILLED)
            cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_im = Image.fromarray(cv2_im)
            draw = ImageDraw.Draw(pil_im)
            font = ImageFont.truetype("simhei.ttf", 25, encoding="utf-8")
            draw.text((left + 20, bottom - 25), name, (255, 255, 255), font=font)
            frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
