# 基于dlib的人脸识别工具,使用face_recognition构建的人脸识别工具集
  
## pip安装
pip3 install face_recognition_util

## Tips:
**由于face_recognition模块中人脸比对部分算法问题需要修改  
在face_recognition目录中找到api.py  
将compare_faces函数替换为以下内容:**

'''
match_list = list(face_distance(known_face_encodings, face_encoding_to_check))  
'''
'''
min_index = match_list.index(min(match_list))  
'''
'''
for (index, value) in enumerate(match_list):  
'''
'''
    match_list[index] = False  
'''
'''
if match_list[min_index] <= tolerance:  
'''
'''
    match_list[min_index] = True  
'''
'''
return match_list  
'''

## 部分函数说明:
convert_to_image:将base64码转换为openCv格式图片，转换错误返回error  
resize_image:将图片转换为指定倍数大小，不指定倍数则默认以基准120大小缩放  
get_face_encoding:获取图片中单个人脸特征点向量  
contrast_faces:人脸比对,可指定检测参数，越小结果越严格  
real_time_comparison:实时人脸比对，将在该函数中启动摄像头进行实时比对  

## 首次安装需要附加依赖环境

numpy,  
dlib(安装报错,请自行编译并安装dlib,可能用到的工具:cmake),  
gevent(非必须,构建flask web应用),  
flask(非必须,构建falsk web应用),  
opencv-python,  
face_recognition  