from cv2 import cv2
import numpy as np

# img = cv.imread()
# img = cv2.imread('image\640.png', 1)
# cv2.imshow('src', img)

if __name__ == "__main__":

    img = cv2.imread("640.png",1)
    img1 = cv2.imread("../640.png")
    # img_gray = cv2.imread("640.png",cv2.IMREAD_GRAYSCALE)
    print(img)
    print("-----------------")
    print(img1)
    # cv2.imshow('image',img)