import cv2 as cv
import numpy as np


#超大图像二值化，采用分割加局部阈值的方法
#由于图像比较大cv.imshow显示不全，我们把图保存，用图像查看器来看
def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + ch, col:cw + col]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 189, 20)
            gray[row: row + ch, col: cw + col] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("F:/result_binary.png", gray)



src = cv.imread('F:001.jpeg')
#cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
#cv.imshow("0", src)
big_image_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()
