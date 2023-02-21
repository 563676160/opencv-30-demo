import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


def keys_demo():
    image = cv.imread("D:/Python/images/lena.png")
    cv.imshow("image", image)
    while True:
        c = cv.waitKey(0)
        # 按数字1
        if c == 49:

            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            cv.imshow("result", gray)
        # 按数字2
        if c == 50:
            hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
            cv.imshow("result", hsv)
        # 按数字3
        if c == 51:
            # 取反操作
            invert=cv.bitwise_not(image)
            cv.imshow("result", invert)
        # 按esc键
        if c == 27:
            break
            return 0;
    cv.destroyAllWindows();

if __name__ == "__main__":
    keys_demo()
