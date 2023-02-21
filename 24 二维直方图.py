import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def hist_demo():
    image = cv.imread("D:/Python/images/face_beauty_test.jpg")
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)

    # channel = [0, 1]，因为我们需要同时处理H和S平面。
    #     # bins = [180, 256]
    #     # 对于H平面为180，对于S平面为256。
    #     # range = [0, 180, 0, 256]
    #     # 色相值介于0和180之间，饱和度介于0和256之间。
    histr=cv.calcHist(hsv,[0,1],None,[180,256],[0,180,0,256])
    plt.imshow(histr,interpolation = 'nearest')
    plt.show()


    # # 图片缩放
    # dst=cv.resize(hsv,(800,800))
    # cv.imshow('dst', dst)
    # # 像素值归一
    # cv.normalize(dst,dst,0,255,dtype=cv.NORM_MINMAX)
    # cv.imshow('dstgg', dst)
    # cv.imshow('image',image)
    # cv.imshow('hsv',hsv)

    cv.waitKey(0)
    return 0

if __name__ == '__main__':
    hist_demo()