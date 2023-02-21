import cv2 as cv
import numpy as np


def     video_demo():
    cap=cv.VideoCapture("D:/Python/images/01.mp4")
    w=cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h=cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps=cap.get(cv.CAP_PROP_FPS)

    # 视频保存
    out=cv.VideoWriter("D:/test.mp4",cv.VideoWriter_fourcc('P','I','M','1'),fps,(np.int(w),np.int(h)),True)
    print(w,h,fps)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()


    while True:
        ret,frame=cap.read()
        if ret is True:
            cv.imshow("video",frame)
            out.write(frame)
            c=cv.waitKey(50)
            if c==27:
                break
    cv.destroyAllWindows()


    cap.release()
    out.release()
if __name__ == '__main__':
    video_demo()