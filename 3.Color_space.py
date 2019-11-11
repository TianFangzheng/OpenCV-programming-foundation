import cv2 as cv
import numpy as np

#提取视频或者图片中的固定颜色    色彩数值图见下图
def extrace_object_demo():
    # capture = cv.VideoCapture("E:/video/fall.mp4")
    # while(True):
    #     ret, frame = capture.read()
    #     if ret == False:
    #         break
    #     hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #     lower_hsv = np.array([0,43,46])
    #     upper_hsv = np.array([10,255,255])
    #     mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
    #     #cv.imshow("video",frame)
    #     cv.imshow("mask",mask)
    #     c = cv.waitKey(40)
    #     if c == 27:
    #         break
    src = cv.imread('F:001.jpg')
    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 0, 0])
    upper_hsv = np.array([180, 255, 46])
    mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
    cv.imshow("0", src)
    cv.imshow("mask", mask)


#色彩空间转换
def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)

#图像通道分离与合并
def color_change(image):
    b, g, r = cv.split(image)
    cv.imshow("blue",b)
    cv.imshow("green",g)
    cv.imshow("red",r)

    image = cv.merge([b,g,r])
    image[:,:,0] = 0   #修改一个蓝色通道全为黑色
    cv.imshow("change image",image)

src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
#color_space_demo(src)     #色彩空间转换
extrace_object_demo()     #提取视频或者图片中的固定颜色
#color_change(src)         #图像通道分离与合并

cv.waitKey(0)
cv.destroyAllWindows()
