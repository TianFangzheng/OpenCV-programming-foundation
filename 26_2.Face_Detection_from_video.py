import cv2 as cv
import numpy as np

def face_detect_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("F:/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 5)  # 第二个参数是移动距离，第三个参数是识别度，越大识别读越高
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 后两个参数，一个是颜色，一个是边框宽度
    cv.imshow("result", image)

capture = cv.VideoCapture(0)
while (True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)  # 对视频做一个镜像对称变化
    face_detect_image(frame)
    c = cv.waitKey(50)
    if c == 27:  # 如果按下Esc键，退出视频
        break
