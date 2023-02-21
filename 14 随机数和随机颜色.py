import cv2 as cv
import numpy as np

def random_demo():
    image = np.zeros((520,520,3),dtype=np.uint8)
    while True:
        xx=np.random.randint(0,520,2,dtype=np.int32)
        yy = np.random.randint(0, 520, 2, dtype=np.int32)
        bgr= np.random.randint(0,255,3,dtype=np.int32)
        cv.line(image,(xx[0],xx[1]),(yy[0],yy[1]),(np.int(bgr[0]),np.int(bgr[1]),np.int(bgr[2])),1,8,0)
        cv.imshow("image",image)
        c=cv.waitKey(100)
        if c==27:
            return 0
            cv.destroyAllWindows()

if __name__=='__main__':
    random_demo()