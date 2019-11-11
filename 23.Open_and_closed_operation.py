import cv2 as cv
import numpy as np


# 图像的开闭操作
def open_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open-result", dst)


def close_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close-result", dst)


src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
open_image(src)
close_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
