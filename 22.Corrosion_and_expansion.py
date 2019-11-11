import cv2 as cv
import numpy as np


# 腐蚀
def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #图像转灰度图
    # 将灰度图转为二值图 ret是阈值 binary是二值图
    ret, binary = cv.threshold(gray, 0 ,255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary', binary)      # 显示二值图像
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 定义覆盖区域的大小
    dst = cv.erode(binary, kernel)                 # 腐蚀操作
    cv.imshow("erode_demo", dst)


# 膨胀
def expand_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #图像转灰度图
    # 将灰度图转为二值图 ret是阈值 binary是二值图
    ret, binary = cv.threshold(gray, 0 ,255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary', binary)      # 显示二值图像
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 定义覆盖区域的大小
    dst = cv.dilate(binary, kernel)                 # 膨胀操作
    cv.imshow("expand_demo", dst)


# 对彩色图像膨胀腐蚀
def color_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 定义覆盖区域的大小
    dst1 = cv.erode(image, kernel)                  # 腐蚀操作
    dst2 = cv.dilate(image, kernel)                 # 膨胀操作
    cv.imshow('color_fushi', dst1)
    cv.imshow('color_pengzhang', dst2)

src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
erode_demo(src)
expand_demo(src)
color_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
