import cv2 as cv
import numpy as np


#均值模糊//均值模糊可以去随机噪声
def blur_demo(image):
    dst = cv.blur(image,(1,15))   #用1*15的模板去模糊图像，步长默认为1
    cv.imshow('blur_demo',dst)


#中值模糊//中值模糊可以去椒盐噪声
def median_bulur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow('median_blur_demo',dst)


#自定义模糊//此处用的是锐化的卷积核
def custom_blur_demo(image):
    kernel = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow('custom_blur_demo',dst)


src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
blur_demo(src)          #均值模糊//均值模糊可以去随机噪声
median_bulur_demo(src)  #中值模糊//中值模糊可以去椒盐噪声
custom_blur_demo(src)   #自定义模糊//此处用的是锐化的卷积核
cv.waitKey(0)
cv.destroyAllWindows()
