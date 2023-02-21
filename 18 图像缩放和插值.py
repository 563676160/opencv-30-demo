import cv2 as cv
import numpy as np

def norm_demo():
    image = cv.imread("D:/Python/images/lena.png")

    h,w,c=image.shape

    # 缩放方法1
    # dst=cv.resize(image,(300,400))

    # 缩放方法2 插值方式自己选择
    # dst=cv.resize(image,(h*2,w*2),interpolation=cv.INTER_CUBIC)

    # 缩放方法3
    dst=cv.resize(image,(0,0),fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)

    cv.imshow("img",image)
    cv.imshow("dst", dst)
    cv.waitKey(0)
    return 0


if __name__ == '__main__':
    norm_demo()