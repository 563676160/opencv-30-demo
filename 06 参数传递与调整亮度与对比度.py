import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


def addWeighted():
    image = cv.imread("D:/Python/images/lena.png")
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    # 亮度和对比度的滑动条
    cv.createTrackbar("lightness", "input", 0, 255, nothing)
    cv.createTrackbar("contrast", "input", 0, 200, nothing)
    blank = np.zeros_like(image)
    while True:
        # 返回得到数值
        light=cv.getTrackbarPos("lightness","input")
        contrast = cv.getTrackbarPos("contrast", "input")/100
        print("lightness：",light,"contrast:",contrast)
        # 使用addWeighted函数
        result=cv.addWeighted(image,contrast,blank,0.5,light)
        cv.imshow("result", result)
        c = cv.waitKey(1)
        if c == 27:
            return
    cv.destroyAllWindows();

if __name__ == "__main__":
    addWeighted()
