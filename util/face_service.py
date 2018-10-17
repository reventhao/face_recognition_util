import face_recognition_util

DECODING_ERROR = "e001"  # 转换编码为图片错误
FACE_NOT_FOUND = "e002"  # 没有找到人脸错误
COMPARE_ERROR = "e003"  # 人脸比对错误


def get_contrast_faces_result(known_image_code, unknown_image_code):
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
        return result
    else:
        result = face_recognition_util.contrast_faces(known_image, unknown_image)
        if result == "nf":
            result = FACE_NOT_FOUND
        elif result == "err":
            result = COMPARE_ERROR
        else:
            result = str(result[0])
    return result
