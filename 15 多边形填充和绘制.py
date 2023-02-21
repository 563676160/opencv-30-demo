import cv2 as cv
import numpy as np

def draw_demo():
    image = cv.imread("D:/Python/images/dog.jpg")
    print(image.shape)
    # 创建一个数组对象
    pts=np.array([[100,100],[350,100],[450,280],[320,450],[80,400]],dtype=int)
    # 绘制多边形
    # cv.polylines(image,[pts],-1,(0,255,255),2,8,0)
    # 填充多边形
    # cv.fillPoly(image,[pts],(0,255,255),8,0)

    cv.drawContours(image,[pts],-1,(255,0,0),-1)

    cv.imshow("dog",image)
    c = cv.waitKey(0)
    if c == 27:
        return 0
    cv.destroyAllWindows()

if __name__=='__main__':
    draw_demo()