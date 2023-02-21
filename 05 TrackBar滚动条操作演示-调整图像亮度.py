import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


def adjust_lightness_demo():
    image = cv.imread("D:/Python/images/lena.png")
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("lightness", "input", 0, 255, nothing)
    blank = np.zeros_like(image)
    while True:
        pos = cv.getTrackbarPos("lightness", "input")
        blank[:, :] = (pos, pos, pos)
        result = cv.add(image, blank)
        cv.imshow("result", result)
        c = cv.waitKey(1)
        if c == 27:
            return
    cv.destroyAllWindows();


if __name__ == "__main__":
    adjust_lightness_demo()
