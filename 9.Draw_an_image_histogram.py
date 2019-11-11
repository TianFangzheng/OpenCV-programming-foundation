import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 绘制图像单通道的直方图
def polt_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show('直方图')


# 绘制图像三通道直方图
def image_hist(image):
    color = ('b','g','r')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist,color=color)
        plt.xlim([0, 256])
    plt.show()


src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
polt_demo(src)
image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows() 
