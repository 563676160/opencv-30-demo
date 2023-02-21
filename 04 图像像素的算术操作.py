import cv2 as cv
import numpy as np

def math_demo():
    image = cv.imread("D:/Python/images/lena.png")
    h,w,c=image.shape  ##返回图片的(高,宽,位深)
    blank=np.zeros_like(image);
    blank[:,:]=(50,50,50)
    cv.imshow("image",image)
    add = cv.add(image,blank)  ##加
    subtract =cv.subtract(image,blank)  ##减

    elementray =np.zeros_like(image)
    elementray[:,:]=(2,2,2)
    multiply =cv.multiply(image,elementray) ##乘
    divide =cv.divide(image,elementray)  ##除
    cv.imshow("blank",blank)
    cv.imshow("add",add)
    cv.imshow("subtract", subtract)
    cv.imshow("multiply",multiply)
    cv.imshow("divide",divide)
    cv.waitKey(0)
    cv.destroyAllWindows();

if __name__=="__main__":
    math_demo()
