import cv2
import os
import numpy as np
import time


# calculate The Phase Only Transform
def PHOT(image):
    # DFT
    F = np.fft.fft2(image)
    # get  magnitude
    M = np.abs(F)
    # Get phase
    P = F / M
    # Reconstruct image from phase
    R = np.abs(np.fft.ifft2(P))
    return R


# get circular image
def getCircle(image):
    temp = np.zeros(image.shape, np.uint8)
    r = 850
    for i in range(1700):
        for j in range(1700):
            lx = abs(i - r)  # 到圆心距离的横坐标
            ly = abs(j - r)  # 到圆心距离的纵坐标
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径

            if l < 825:
                temp[i, j] = image[i, j]
            else:
                temp[i, j] = 0
    return temp

if __name__ == '__main__':
    path = './original/'
    filenames = os.listdir(path)
    for filename in filenames:
        time_beg = time.time()
        # read image
        img = cv2.imread(path + filename, 0)
        #img = img[595:2295, 1515:3215]

        '''get circular area of the ball, but useless and time-consuming'''
        # img_circle = getCircle(img)
        # cv2.imwrite('temp.bmp', _circle)

        # Get PHOT
        r = PHOT(img)

        # GaussianBlur
        img_Ed = cv2.GaussianBlur(r, (5, 5), 3)

        # calculate mean and variance
        mean, stddv = cv2.meanStdDev(img_Ed)

        # Compute distance Euclidean
        #img_Ed = np.power(img_G - mean, 2)
        img_Ed = np.abs(img_Ed - mean)

        img_normal = np.zeros(img_Ed.shape)
        cv2.normalize(img_Ed, img_normal, 0, 255, cv2.NORM_MINMAX)
        img_normal = cv2.convertScaleAbs(img_normal)
        #img_nm = cv2.adaptiveThreshold(img_normal, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 13, 2)
        det, img_binary = cv2.threshold(img_normal, 50, 255, cv2.THRESH_BINARY)

        # dilate
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        img_dilated = cv2.dilate(img_binary, kernel)

        '''this part is to test whether defection is detected'''
        # original image and dilated image bitwise_and
        # img_and = cv2.bitwise_and(img_dilated, img)

        # save result image
        cv2.imwrite(filename, img_binary)
        time_end = time.time()
        print("{}: {:.5f}s".format(filename, time_end - time_beg))
