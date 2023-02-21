import cv2 as cv
import numpy as nu

def pixel_demo():
    image = cv.imread("D:/Python/images/lena.png")
    h,w,c=image.shape  ##返回图片的(高,宽,位深)
    cv.imshow("input",image)
    # 获取像素值
    for row in range(h):
        for col in range(w):
            b,g,r = image[row,col]
            image[row,col]=[255-b,255-g,255-r]
    cv.imshow("output", image)
    cv.imwrite("D:/Python/images/pixel_demo_result.png",image)
    cv.waitKey(0)
    cv.destroyAllWindows();

if __name__=="__main__":
    pixel_demo()
