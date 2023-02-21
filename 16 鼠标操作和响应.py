import cv2 as cv
import numpy as np

x1 = -1
x2 = -1
y1 = -1
y2 = -1

image = cv.imread("D:/Python/images/lena.png")
b1 = np.copy(image)


def mouse_drawing(event, x, y, flags, param):
    # 全局调用变量
    global x1, x2, y1, y2
    # 左键点击事件
    if event == cv.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
    # 鼠标滑动事件
    if event == cv.EVENT_MOUSEMOVE:
        # 在绘制之前要限制鼠标在点击左键之前的操作所以x1，y1小于1就不绘制
        if x1 < 0 or y1 < 0:
            return
        x2 = x
        y2 = y
        # 要让只往右下角移动才有框框所以要给差值dx，dy
        dx = x2 - x1
        dy = y2 - y1
        if dx > 0 and dy > 0:
            # 持续刷新图片，让图片上只有一个方框
            image[:, :] = b1[:, :]
            cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 1, 8, 0)

    # 鼠标左键抬起事件
    if event == cv.EVENT_LBUTTONUP:
        # 在绘制之前要限制鼠标在点击左键之前的操作所以x1，y1小于1就不绘制
        if x1 < 0 and y1 < 0:
            return
        x2 = x
        y2 = y
        # 要让只往右下角移动才有框框所以要给差值dx，dy
        dx = x2 - x1
        dy = y2 - y1

        if dx > 0 and dy > 0:
            image[:, :] = b1[:, :]
            cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 1, 8, 0)
        x1 = -1
        x2 = -1
        y1 = -1
        y2 = -1


def mouse_demo():
    cv.namedWindow("Mouse", cv.WINDOW_AUTOSIZE)
    # 第二个参数是回调函数
    cv.setMouseCallback("Mouse", mouse_drawing)
    while True:
        cv.imshow("Mouse", image)
        c = cv.waitKey(10)
        if c == 27:
            return 0
    cv.destroyAllWindows()


if __name__ == '__main__':
    mouse_demo()
