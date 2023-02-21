import cv2 as cv
import numpy as np
def color_space_channel():
    image=cv.imread("D:/Python/images/greenback.png")
    cv.imshow("image",image)
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow('hvs',hsv)

    # 绿幕变成白色 人像变黑
    mask = cv.inRange(hsv,(35,43,46),(77,255,255))
    # 翻转一下绿幕变黑，人像变白
    cv.bitwise_not(mask,mask)
    cv.imshow("mask",mask)
    # 这里的前面mask=是找出与的面积 后面的是掩膜
    result=cv.bitwise_and(image,image,mask=mask)
    cv.imshow("result", result)
    c=cv.waitKey(0)
    if c==27:
        return 0
    cv.destroyAllWindows()

if __name__ == '__main__':
    color_space_channel()