import cv2 as cv
import numpy as np


#全局阈值OSTU方法
def threshold_demo(image):
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gary, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value OSTU %s"%ret)
    cv.imshow('binary_OSTU',binary)


#全局阈值TRIANGLE方法
def threshold_2_demo(image):
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gary, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold value TRIANGLE %s"%ret)
    cv.imshow('binary_TRIANGLE',binary)


#全局阈值自设阈值方法
def threshold_3_demo(image):
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gary, 177, 255, cv.THRESH_BINARY)
    #可以通过修改第三个参数cv.THRESH_BINARY，做效果反转，截断等效果
    print("threshold value self177 %s"%ret)
    cv.imshow('binary_self',binary)


#局部阈值或者自适应阈值的方法(均值)
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("self_mean", binary)


#局部阈值或者自适应阈值的方法(高斯均值)
def local_1_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("self_gaosi", binary)




src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
threshold_demo(src)
threshold_2_demo(src)
threshold_3_demo(src)
local_threshold(src)
local_1_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()
