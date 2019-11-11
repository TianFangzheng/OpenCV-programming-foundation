import cv2 as cv
import numpy as np


#两张图片相加（两张图片的大小要一致）
def add_demo(m1,m2):
    des = cv.add(m1,m2)
    cv.imshow('add',des)


#两张图片相减（两张图片的大小要一致）
def subtrace_demo(m1,m2):
    des = cv.subtract(m1,m2)
    cv.imshow('sub',des)

#两张图片相除（两张图片的大小要一致）
def divide_demo(m1,m2):
    des = cv.divide(m1,m2)
    cv.imshow('div',des)

#两张图片相乘（两张图片的大小要一致）
def multiply_demo(m1,m2):
    des = cv.multiply(m1,m2)
    cv.imshow('mul',des)

#两张图片与或非（两张图片的大小要一致）
def logic_demo(m1,m2):
    yu = cv.bitwise_and(m1,m2)
    huo = cv.bitwise_or(m1,m2)
    fei = cv.bitwise_not(m1)       #非  就是按位取反

    cv.imshow('yu',yu)
    cv.imshow('huo',huo)
    cv.imshow('fei',fei)

#调整图像对比度与亮度
def contrast_brightness_demo(image,c,b):  #这里c代表对比度，b代表亮度
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    det = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow('con-bri',det)


#计算图像的均值与方差
def others(m1,m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)

    print(M1)   #输出均值
    print(M2)

    print(dev1)  #输出方差
    print(dev2)



src1 = cv.imread('F:001.jpg')
src2 = cv.imread('F:002.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("img1", src1)
cv.imshow('img2',src2)
add_demo(src1,src2)         ##两张图片相加（两张图片的大小要一致）
subtrace_demo(src1,src2)    #两张图片相减（两张图片的大小要一致）
divide_demo(src1,src2)      #两张图片相除（两张图片的大小要一致）
multiply_demo(src1,src2)    #两张图片相乘（两张图片的大小要一致）
logic_demo(src1,src2)         #两张图片与或非（两张图片的大小要一致）
contrast_brightness_demo(src1,1.2,20)  #调整图像对比度与亮度
others(src1,src2)             #计算图像的均值与方差
# print(src1.shape)
# print(src2.shape)
cv.waitKey(0)
cv.destroyAllWindows()
