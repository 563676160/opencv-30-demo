import cv2 as cv
import numpy as np

def norm_demo():
    image = cv.imread("D:/Python/images/lena.png")
    # # 图片可以归一化，使范围在0-1之间
    # cv.imshow("person",image/255.0)
    # print(image/255.0)

    # 同样的，也可以强转成浮点数在运算 这个会变得很白，必选要np.float32(image)/255才可以
    # cv.imshow("person", np.float32(image))
    # print(np.float32(image))

    # 这样子才正确
    # cv.imshow("person", np.float32(image)/255)
    # print(np.float32(image)/255)

    # 浮点数归一化操作
    result=np.zeros_like(np.float32(image))
    cv.normalize(np.float32(image),result,0,1,cv.NORM_MINMAX,dtype=cv.CV_32F)
    # cv.imshow("person",result)
    # 浮点数变字节数
    cv.imshow("person",np.uint8(result*255))

    print(result*255)

    cv.waitKey(0)
    return 0


if __name__ == '__main__':

    norm_demo()