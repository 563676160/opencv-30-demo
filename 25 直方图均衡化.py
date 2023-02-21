import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def eqhist_demo():
    # 进行图像均衡必须要将图片变成灰度图
    image = cv.imread("D:/Python/images/face_beauty_test.jpg",cv.IMREAD_GRAYSCALE)
    cv.imshow('image',image)
    result= cv.equalizeHist(np.uint8(image))
    cv.imshow('result',result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    eqhist_demo()