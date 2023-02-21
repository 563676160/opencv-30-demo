import cv2 as cv
import numpy as np

def flip():
    image = cv.imread("D:/Python/images/lena.png")
    # 翻转函数
    flip=cv.flip(image,1)
    cv.imshow("img", image)
    cv.imshow("flip", flip)
    cv.waitKey(0)
    return 0

if __name__ == '__main__':
    flip()