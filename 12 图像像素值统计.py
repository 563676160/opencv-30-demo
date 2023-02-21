# 一个像素点有5个元素  坐标值 RGB0-255
# 有效信息的像素方差不为0

import cv2 as cv
import numpy as np

def pixel_stat():
    image=cv.imread("D:/Python/images/example.png")
    cv.imshow("image",image)
    print(image.shape)
    # 获取某色彩通道的最大值
    print(np.max(image[:,:1]))
    # 获取某色彩通道的最小值
    print(np.amin(image[:, :1]))
    # 获取色彩通道中所有像素的均值与方程
    means,stddev=cv.meanStdDev(image)
    print(means,stddev)
    c=cv.waitKey(0)
    if c==27:
        return 0
    cv.destroyAllWindows()


if __name__ == '__main__':
    pixel_stat()