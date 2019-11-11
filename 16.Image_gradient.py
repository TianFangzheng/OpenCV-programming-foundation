import cv2 as cv
import numpy as np


#图像梯度：索贝尔算子
def sobel_image(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)#x方向导数
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)#y方向导数
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("X_sob", gradx)#颜色变化在水平分层
    cv.imshow("Y_sob", grady)#颜色变化在垂直分层
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("xy_sob", gradxy)

#图像梯度：scharr算子：增强边缘
def scharr_image(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)#x方向导数
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)#y方向导数
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("X_sch", gradx)#颜色变化在水平分层
    cv.imshow("Y_sch", grady)#颜色变化在垂直分层
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("xy_sch", gradxy)

#拉普拉斯算子
def lapalian_image(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls", lpls)

#图像锐化
def custom_blur_demo(image):
    kernel = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow('custom_blur_demo',dst)


src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
sobel_image(src)
scharr_image(src)
lapalian_image(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
