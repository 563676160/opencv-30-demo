import cv2 as cv
import numpy as np


def rotate():
    image = cv.imread("D:/Python/images/lena.png")
    h, w, c = image.shape
    # opencv自带的旋转函数rotate：
    # dst=cv.rotate(image,rotateCode=cv.ROTATE_180)

    # 定义一个2x3的旋转矩阵
    M = np.zeros((2, 3), dtype=np.float32)
        # 定义旋转角度
    alpha = np.cos(np.pi / 4.0)
    beta = np.sin(np.pi / 4.0)
    print("alpha : ", alpha)

        # 初始化旋转矩阵
    M[0, 0] = alpha
    M[1, 1] = alpha
    M[0, 1] = beta
    M[1, 0] = -beta
        # 找到图像的中心结点
    centerx=w/2
    centery=h/2
        # 计算矩阵旋转从像素左上角变成中心位置的偏移量
    tx = (1 - alpha) * centerx - beta * centery
    ty = beta * centerx + (1 - alpha) * centery
        # 初始化矩阵
    M[0, 2] = tx
    M[1, 2] = ty


    # 函数warpAffine支持任意角度的旋转，通过定义M矩阵实现
    # 这里dsize大小还是原图大小，所以要改大一点
    # dst = cv.warpAffine(image, M,(w,h))

    # 计算出新矩阵的大小
    bound_w = int(h * np.abs(beta) + w * np.abs(alpha))
    bound_h = int(h * np.abs(alpha) + w * np.abs(beta))
    M[0, 2] += bound_w/2-centerx
    M[1, 2] += bound_h/2-centery
    dst = cv.warpAffine(image, M, (bound_w, bound_h),borderValue=(0,255,0))

    cv.imshow("img", image)
    cv.imshow("dst", dst)
    cv.waitKey(0)
    return 0


if __name__ == '__main__':
    rotate()
