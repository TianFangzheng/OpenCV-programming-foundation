import cv2 as cv
import numpy as np


# 对象测量
# 计算每个轮廓的弧长和面积 单位是像素
# 多边形拟合
def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #图像转灰度图
    # 将灰度图转为二值图 ret是阈值 binary是二值图
    ret, binary = cv.threshold(gray, 0 ,255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print('threshold value: %s'%ret)  # 把阈值打印出来
    cv.imshow('binary image',binary)  # 把二值图显示出来
    # 找目标的轮廓
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i , contour in enumerate(contours):
        area = cv.contourArea(contour)  # 计算轮廓的面积
        print('area',area)
        x, y, w, h = cv.boundingRect(contour) # 计算轮廓外接矩形
        rate = min(w, h)/max(w,h)  # 计算长宽比
        print('rate',rate)
        mm = cv.moments(contour) # 计算轮廓的几何矩
        print(type(mm))
        # 找轮廓的中心位置
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        # 用个黄色小圆圈把几何图形的中心位置绘制出来
        cv.circle(image, (np.int(cx) , np.int(cy)), 3, (0,255,255), -1)
        # 用红色框框把外接矩形绘制出来
        cv.rectangle(image, (x,y), (x+w, y+h),(0,0,255), 2)
    cv.imshow('measure_contours',image)

# 多边形拟合（为了看起来方便，画到二值图上）
def haha_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #图像转灰度图
    # 将灰度图转为二值图 ret是阈值 binary是二值图
    ret, binary = cv.threshold(gray, 0 ,255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)  # 二值图上就可以画彩色的了
    # 找目标的轮廓
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i , contour in enumerate(contours):
        mm = cv.moments(contour) # 计算轮廓的几何矩
        print(type(mm))
        # 找轮廓的中心位置
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        # 用个黄色小圆圈把几何图形的中心位置绘制出来
        cv.circle(dst, (np.int(cx) , np.int(cy)), 3, (0,255,255), -1)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] > 6:      # 如果绘制的边大于6，一般是圆，就绘制出来
            cv.drawContours(dst, contours, i, (0,255,0), 2)
        if approxCurve.shape[0] == 4:     # 如果绘制的边恒为4，四边形，就绘制出来
            cv.drawContours(dst, contours, i, (255,0,0), 2)
        if approxCurve.shape[0] == 6:
            cv.drawContours(dst, contours, i, (0,0,255), 2)
    cv.imshow('binin_contours',dst)


src = cv.imread('F:0909.png')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
measure_object(src)
# haha_object(src)
cv.waitKey(0)
cv.destroyAllWindows()
