import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def conv_demo():
    image = cv.imread("D:/Python/images/lena.png")
    cv.imshow("image",image)
    # 高斯滤波只有是（0，0），后面才可以用这个参数
    result=cv.GaussianBlur(image,(0,0),15)
    cv.imshow("result",result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    conv_demo()