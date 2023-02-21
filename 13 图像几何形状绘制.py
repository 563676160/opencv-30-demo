import cv2 as cv
import numpy as np

def draw_demo():
    image = cv.imread("D:/Python/images/dog.jpg")
    # 绘制长方形
    cv.rectangle(image,(200,300),(400,500),(0,0,255),3,2,0)
    # 绘制⚪
    cv.circle(image,(250,250),50,(0,255,0),-1)
    # 绘制线
    cv.line(image,(200,300),(400,500),(255,0,0),4)
    # 绘制字体
    cv.putText(image,"dog and ",(200,200),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,255),2,8)
    cv.imshow("dog",image)
    c = cv.waitKey(0)
    if c == 27:
        return 0
    cv.destroyAllWindows()

if __name__=='__main__':
    draw_demo()