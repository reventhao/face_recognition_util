import requests


def get_base64_code(data, url,):
    result = requests.post(url, data)
    return result.json().data.xp
