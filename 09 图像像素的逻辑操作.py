import cv2 as cv
import numpy as np


def bitwise():
    image1 = np.zeros((400, 400, 3), dtype=np.uint8)
    image1[:, :] = (0, 255, 255)
    image2 = np.zeros((400, 400, 3), dtype=np.uint8)
    image2[:, :] = (255, 0, 0)
    cv.imshow("image1", image1)
    cv.imshow("image2", image2)
    result1=cv.bitwise_and(image1,image2)
    result2 = cv.bitwise_or(image1, image2)
    cv.imshow("result1", result1)
    cv.imshow("result2", result2)
    c= cv.waitKey(0)
    if c == 27:
        return 0
    cv.destroyAllWindows()

if __name__ == '__main__':
    bitwise()

