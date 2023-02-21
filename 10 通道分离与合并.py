import cv2 as cv
import numpy as np


def channel():
    image=cv.imread("D:/Python/images/lena.png")
    cv.imshow("image",image)
    cv.imshow("b0",image[:,:,0])
    cv.imshow("b1",image[:,:,1])
    cv.imshow("b2",image[:,:,2])

    mv = cv.split(image)
    mv[1][:,:]=255
    result=cv.merge(mv)
    cv.imshow("result",result)

    dst = np.zeros(image.shape,dtype=np.uint8)
    cv.mixChannels([image],[dst],fromTo=[2,0,1,1,0,2])
    cv.imshow("dst",dst)


    c= cv.waitKey(0)
    if c == 27:
        return 0
    cv.destroyAllWindows()

if __name__ == '__main__':
    channel()

