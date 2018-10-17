#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: reventhao
# Mail: ren895873@gmail.com
# Created Time:  2018-10-15 11:47:34
#############################################


from setuptools import setup

setup(
    name="face_recognition_util",
    version="0.1.2",
    keywords=("face_recognition_util"),
    description="face recognition tools",
    long_description="Provide Base64 transcoding,Picture zoom,Face comparison,and real-time comparison",
    license="MIT Licence",

    url="https://github.com/reventhao/face_recognition_util",
    author="reventhao",
    author_email="ren895873@gmail.com",

    packages=[
        'face_recognition_util',
    ],
    package_dir={'face_recognition_util': 'face_recognition_util'},
    include_package_data=True,
    platforms="any",
    install_requires=["numpy", "dlib", "gevent", "flask", "opencv-python", "face_recognition", "Pillow"]
)
