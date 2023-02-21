import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def conv_demo():
    image = cv.imread("D:/Python/images/lena.png")
    cv.imshow("image",image)
    # 均值滤波
    result=cv.blur(image,(5,5))
    cv.imshow("result",result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    conv_demo()