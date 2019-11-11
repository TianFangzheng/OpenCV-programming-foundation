import cv2 as cv
import numpy as np

#计算每一个像素，并对每一个像素反转
def accesss_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height:%s,   width:%s,   channels:%s"%(height,width,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv;
    cv.imshow("1",image)

#自己创建一个图像
def creat_image():
    img = np.zeros([400,400,3],np.uint8)  #初始化全是0的数组
    img[:,:,0]=np.ones([400,400])*255     #对第一个通道赋值，初始值为1，乘255后应该显示蓝色
    cv.imshow("2",img)


#numpy简单用法
def num():
    m1 = np.ones([3,3],np.int)
    m1.fill(66)
    print("m1:",m1)
    m2 = m1.reshape([1,9])
    print("m2",m2)

src=cv.imread('F:001.jpg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)

cv.imshow("0",src)
t1 = cv.getTickCount()
accesss_pixels(src)
creat_image()
num()
t2 = cv.getTickCount()
t = (t2-t1)/cv.getTickFrequency()
print("用时%s s"%t)

cv.waitKey(0)
cv.destroyAllWindows()
