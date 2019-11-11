import cv2 as cv
import numpy as np


# 分水岭算法
def watershed_image():
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)  # 利用边缘滤波，去除噪点

    # gray\binary image 灰度二值图像
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary_image", binary)

    # morphology operation  形态学操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))   #结构元素
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)  #连续两次开操作
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor_opt", sure_bg)

    # distance transform 对上面的mb进行距离变换
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("distance", dist_output * 70)

    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin", surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed transfrom 分水岭变换
    markers += 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow("result", src)


src = cv.imread('F:00.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
watershed_image()
cv.waitKey(0)
cv.destroyAllWindows()
