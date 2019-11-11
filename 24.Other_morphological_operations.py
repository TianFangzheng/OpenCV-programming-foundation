import cv2 as cv
import numpy as np


# 顶帽操作：原图像与开操作之间的差值图像
def top_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    # 彩图转灰度
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 定义尺度大小
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)   #顶帽操作
    cimage = 100   #  定义一个常规数字
    dst = cv.add(dst, cimage)   # 把原图搞亮100
    cv.imshow("tophat", dst)

# 黑帽操作：闭操作图像与源图像的差值图像
def black_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    # 彩图转灰度
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 定义尺度大小
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)   #顶帽操作
    cimage = 100   #  定义一个常规数字
    dst = cv.add(dst, cimage)   # 把原图搞亮100
    cv.imshow("blackhat", dst)

# 基本梯度>基本梯度是用膨胀后的图像减去腐蚀后的图像得到差值图像，
# 称为梯度图像也是opencv中支持的计算形态学梯度的方法，
# 而此方法得到梯度有被称为基本梯度
def gradient1_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    # 彩图转灰度
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 定义尺度大小
    dst = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)   #顶帽操作
    cv.imshow("jiBenTiDu", dst)


# 内部梯度>是用原图像减去腐蚀之后的图像得到差值图像，称为图像的内部梯度
# 外部梯度>图像膨胀之后再减去原来的图像得到的差值图像，称为图像的外部梯度
def gradient2_demo(image):
    kernel= cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em)  # 内梯度
    dst2 = cv.subtract(dm, image)  # 外梯度
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)



src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
top_hat_demo(src)
black_hat_demo(src)
gradient1_demo(src)
gradient2_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
