#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time:  2018-1-23 19:17:34
#############################################


from setuptools import setup

setup(
    name="face_recognition_util",
    version="0.0.5",
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
