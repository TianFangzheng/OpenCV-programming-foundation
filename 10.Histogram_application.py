import cv2 as cv
import numpy as np


# 全局的直方图均衡化(对灰度图而言的)，是图像对比度增强的一个手段
def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    det = cv.equalizeHist(gray)
    cv.imshow('gray',gray)
    cv.imshow('equalHist_demo',det)


# 局部自适应直方图均衡化(对灰度图而言的)，是图像对比度增强的一个手段
def clahe_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    det = clahe.apply(gray)
    cv.imshow('clahe_demo',det)


#创建彩色的三通道直方图
def creat_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index),0] = rgbHist[np.int(index),0]+1
    return rgbHist


#计算两张图片直方图的相关性（式距离/相关性/卡方）
def hist_compare(image1, image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print('巴式距离：%s, 相关性：%s， 卡方：%s'%(match1, match2,match3))


src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
equalHist_demo(src)      # 全局的直方图均衡化(对灰度图而言的)
clahe_demo(src)          # 局部自适应直方图均衡化
image2 = cv.imread('F:002.jpg')
hist_compare(src, image2)   #计算两张图片直方图相关性
cv.waitKey(0)
cv.destroyAllWindows()
