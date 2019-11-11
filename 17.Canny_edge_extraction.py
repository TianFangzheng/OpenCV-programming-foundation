import cv2 as cv
import numpy as np

def edge_image(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    cv.imshow("canny_edge", edge_output)   #灰度边缘
    dst = cv.bitwise_and(image, image, mask=edge_output)   #将灰度图通过与原图相交还原为彩色
    cv.imshow("color_edge", dst)


src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
edge_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
