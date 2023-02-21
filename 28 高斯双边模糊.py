import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def bifilter():
    image = cv.imread("D:/Python/images/lena.png")
    cv.imshow("image",image)
    result=cv.bilateralFilter(image,0,100,10)
    cv.imshow("result",result)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    bifilter()