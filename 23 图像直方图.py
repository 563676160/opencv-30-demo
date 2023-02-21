import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def hist_demo():
    image = cv.imread("D:/Python/images/face_beauty_test.jpg")


    # 只画一个图片,用的线条
    # hist = cv.calcHist([image], [0], None, [256], [0, 256])
    # plt.hist(image.ravel(),256,[0,256])
    # plt.show()
    # cv.imshow("image",image)

    # 三个颜色表示全部的颜色在一个图中
    # color=('b','g','r')
    # cv.imshow('image',image)
    # for i,color in enumerate(color):
    #     hist = cv.calcHist([image], [i], None, [256], [0, 256])
    #     plt.plot(hist,color=color)
    #     plt.xlim([0,256])
    # plt.show()

    # 掩码的操作
    mask = np.zeros(image.shape[:2], np.uint8)
    mask[100:, 100:] = 255
    masked_img = cv.bitwise_and(image, image, mask=mask)
    hist_full = cv.calcHist([image], [0], None, [256], [0, 256])
    hist_mask = cv.calcHist([image], [0], mask, [256], [0, 256])
    plt.subplot(221), plt.imshow(image, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show()

    cv.waitKey(0)
    return 0

if __name__ == '__main__':
    hist_demo()