import cv2 as cv
import numpy as np


#选图片的感兴趣区域(ROI)，对感兴趣区域进行处理
def roi_demo(image):
    face = image[35:290,45:260]       #把脸部提取出来
    gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
    backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)   #黑白转换为彩色图，只是从单通道变为多通道，还是黑白的
    image[35:290, 45:260] = backface    #把原来的部分用黑白的替换掉
    cv.imshow('face',backface)
    cv.imshow('roi_deom',image)


#泛洪填充-彩色图像进行（连通填充）
def fill_color_demo(image):
    copyImg = image.copy()
    h,w = image.shape[:2]   #这里是把彩色图像的高和宽提取出来
    mask = np.zeros([h+2,w+2],np.uint8)   #mask就是要进行+2处理，类型必须是uint8(必须是单通道8位)
    cv.floodFill(copyImg,mask,(1,1),(0,255,0),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    #floodFill，这个函数，（1，1）代表要处理图像的起始点；(0,255,0)代表要填充的颜色，
    #(100,100,100)代表低值，即（1,1）这个点的像素值各通道减去100，
    #(50,50,50)代表高值，即（1,1）这个点的像素值各通道加上50。
    #以（1，1）位置为起始点，搜索填充
    cv.imshow('fill_color_demo',copyImg)

#泛洪填充--二值填充
def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:]=255
    cv.imshow('fill_binary',image)

    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,255,0),cv.FLOODFILL_MASK_ONLY)
    #这个位置要注意，FLOODFILL_MASK_ONLY填充区域必须是无值才会填充
    cv.imshow('fill binary',image)


src = cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow("0", src)
# roi_demo(src)           #选图片的感兴趣区域(ROI)，对感兴趣区域进行处理
# fill_color_demo(src)    #泛洪填充-彩色图像进行（连通填充）
fill_binary()           #泛洪填充--二值填充
cv.waitKey(0)
cv.destroyAllWindows()
