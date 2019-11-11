import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#直方图反向投影(可以寻找与直方图一致的区域，类似于模板)
def back_projection_demo():
    sample = cv.imread('F:003.png')
    target = cv.imread('F:001.jpg')
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow('sample', sample)
    cv.imshow('target', target)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[5,5],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    cv.imshow('backProjectionDemo',dst)

  
#2D直方图计算与显示
def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
    cv.imshow('hist2d',hist)
    plt.imshow(hist,interpolation='nearest')
    plt.title('2D Histogram')
    plt.show()


# src = cv.imread('F:001.jpg')
# #cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow("0", src)
# hist2d_demo(src)
back_projection_demo()
cv.waitKey(0)
cv.destroyAllWindows()
