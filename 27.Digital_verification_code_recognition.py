import cv2 as cv
import numpy as np
from PIL import Image
import  pytesseract as tess

def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)   # 转灰度图
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 转二值图
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 6))  # 设置尺度大小
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # 开操作
    cv.imshow('bb',binl)
    cv.bitwise_not(binl, binl)     # 反转图像
    textImage = Image.fromarray(binl)    # 将图片转成字符串
    text = tess.image_to_string(textImage)   # 识别字符串内容
    print("result", text)

src = cv.imread('F:99.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
recognize_text()
cv.waitKey(0)
cv.destroyAllWindows()
