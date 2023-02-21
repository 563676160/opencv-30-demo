import cv2 as cv
import numpy as np

def     video_demo():
    # cap=cv.VideoCapture(0)
    cap=cv.VideoCapture("D:/Python/images/01.mp4")
    w=cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h=cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps=cap.get(cv.CAP_PROP_FPS)
    print(w,h,fps)
    # 检测视频是否被打开
    if not cap.isOpened():
        print("Cannot open camera")
        exit()


    while True:
        ret,frame=cap.read()
        if ret is True:
            cv.imshow("video",frame)
            c=cv.waitKey(50)
            if c==27:
                break
    cv.destroyAllWindows()


    cap.release()

if __name__ == '__main__':
    video_demo()