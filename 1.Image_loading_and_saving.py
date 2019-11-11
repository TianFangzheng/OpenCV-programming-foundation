import cv2 as cv
import numpy as np

#打开摄像头，读取视频流
def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame=capture.read()
        frame = cv.flip(frame,1)   #对视频做一个镜像对称变化
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:   #如果按下Esc键，退出视频
            break

#输出图片的各个参数
def get_image_info(image):
    print(type(image))    #图片的类型
    print(image.shape)    #图片大小  长 宽 通道
    print(image.size)     #图片的大小   是 长*宽*通道数 的结果
    print(image.dtype)    #图片数字内容的类型
    pixel_date = np.array(image)   #读取图片中的每个像素值
    print(pixel_date)


src=cv.imread('F:001.jpg')
get_image_info(src)
video_demo()
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite("E:/00.png",gray)

cv.imshow("0",src)
cv.waitKey(0)
cv.destroyAllWindows()
