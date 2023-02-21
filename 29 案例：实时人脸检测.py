import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def face_detection_demo():
    model_bin="D:\Python\Opencv_demo\model\opencv_face_detector_uint8.pb"
    config_text="D:\Python\Opencv_demo\model\opencv_face_detector.pbtxt"
    # OpenCV 3.3版本开始，加入了对深度学习网络的支持，
    # 即DNN模块，它支持主流的深度学习框架生成与到处模型的加载。
    net=cv.dnn.readNetFromTensorflow(model=model_bin,config=config_text)



    cap=cv.VideoCapture("D:/Python/images/example_dsh.mp4")
    while True:
        ret, frame = cap.read()
        h,w,c=frame.shape
        if ret is not True:
            break
            # 将图像处理成4维
        blob=cv.dnn.blobFromImage(frame,1.0,(300,300),(104.0,177.0,123.0),False,False)
        net.setInput(blob)
        outs=net.forward() #1x1xNx7
        for detection in outs[0, 0, :, :]:
            score = float(detection[2])
            if score > 0.5:
                left = detection[3] * w
                top = detection[4] * h
                right = detection[5] * w
                bottom = detection[6] * h
                cv.rectangle(frame,(np.int(left),np.int(top)),(np.int(right),np.int(bottom)),(0,255,0),2,8,0)
            cv.imshow("frame",frame)
            c=cv.waitKey(1)
            if c==27:
                break


if __name__ == '__main__':
    face_detection_demo()
