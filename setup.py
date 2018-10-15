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
    version="0.0.8",
    keywords=("face_recognition_util"),
    description="time and path tool",
    long_description="time and path tool",
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
    install_requires=["numpy", "dlib", "gevent", "flask", "opencv-python", "face_recognition"]
)
