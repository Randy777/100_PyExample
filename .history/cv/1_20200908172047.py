from cv2 import cv2
import numpy as np

# img = cv.imread()
# img = cv2.imread('image\640.png', 1)
# cv2.imshow('src', img)

if __name__ == "__main__":
    print(cv2.__version__)
    img = cv2.imread('640.png')
    print(img)