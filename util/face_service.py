import face_recognition_util

DECODING_ERROR = "001"  # 转换编码为图片错误
FACE_NOT_FOUND = "002"  # 没有找到人脸错误
COMPARE_ERROR = "003"  # 人脸比对错误
SAME_PERSON = "yes"  # 同一个人
NOT_SAME_PERSON = "no"  # 不是同一个人


def get_contrast_faces_result(known_image_code,unknown_image_code):
    """
    return contrast result
    :param known_image_code:
    :param unknown_image_code:
    :return:
    """
    known_image = face_recognition_util.convert_to_image(known_image_code)
    unknown_image = face_recognition_util.convert_to_image(unknown_image_code)
    if isinstance(known_image, str) or isinstance(unknown_image, str):
        result = DECODING_ERROR
    else:
        result = face_recognition_util.contrast_faces(known_image, unknown_image)
        if result == "nf":
            result = FACE_NOT_FOUND
        elif result == "err":
            result = COMPARE_ERROR
        elif result:
            result = SAME_PERSON
        else:
            result = NOT_SAME_PERSON
    return result
