import cv2 as cv
import numpy as np
 

#高斯双边模糊，图像差异大的位置不进行模糊处理，可以有效的保留边缘信息
def bi_demo(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow('bi_demo',dst)


#均值迁移模糊，图像差异大的位置不进行模糊处理，可以有效的保留边缘信息
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow('shift demo',dst)

src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
bi_demo(src)     #高斯双边模糊
shift_demo(src)  #均值迁移模糊
cv.waitKey(0)
cv.destroyAllWindows()
