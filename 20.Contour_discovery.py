import cv2 as cv
import numpy as np


#轮廓发现
def contous_image(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i,contou in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 4)
    cv.imshow("lunkuo", image)
    for i,contou in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 255, 255), -1)
    cv.imshow("lunkuotianchong", image)


src = cv.imread('F:00.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
contous_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
