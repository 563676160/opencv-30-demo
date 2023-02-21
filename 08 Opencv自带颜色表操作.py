import cv2 as cv
import numpy as np


def color_table_demo():
    colormap = [
        cv.COLORMAP_HOT,
        cv.COLORMAP_HSV,
        cv.COLORMAP_JET,
        cv.COLORMAP_MAGMA,
        cv.COLORMAP_COOL,
        cv.COLORMAP_SPRING,
        cv.COLORMAP_SUMMER,
        cv.COLORMAP_AUTUMN,
        cv.COLORMAP_WINTER,
        cv.COLORMAP_BONE,
        cv.COLORMAP_CIVIDIS,
        cv.COLORMAP_HOT,
        cv.COLORMAP_DEEPGREEN,
        cv.COLORMAP_INFERNO,
        cv.COLORMAP_OCEAN,
        cv.COLORMAP_PARULA,
        cv.COLORMAP_PINK,
        cv.COLORMAP_PLASMA,
        cv.COLORMAP_RAINBOW,
        cv.COLORMAP_TURBO,
        cv.COLORMAP_TWILIGHT,
        cv.COLORMAP_TWILIGHT_SHIFTED,
        cv.COLORMAP_VIRIDIS
    ]
    index = 0

    image = cv.imread("D:/Python/images/lena.png")
    cv.imshow("image", image)
    while True:
        dst=cv.applyColorMap(image,colormap[index%3])
        index+=1
        cv.imshow("color style",dst)
        c = cv.waitKey(1000)
        if c==27:
            return 0;
    cv.destroyAllWindows();

if __name__ == "__main__":
    color_table_demo()
