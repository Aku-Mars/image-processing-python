# Melakukan proses Image Filtering
import cv2
import numpy as np

image = cv2.imread('miaw.jpg')

print('1. Filter blur biasa')
print('2. filter linear : averaging')
print('3. filter non-linear median blur')
input = int(input("Masukkan nilai : "))

if input == 1:
    # blur image
    blur = cv2.blur(image, (10, 10))
    result = np.hstack((image, blur))
    print(blur.flatten()[:50])
elif input == 2:
    # averaging image (linear filtering)
    set_kernel = np.ones((10, 10), np.float32) / 25
    dst = cv2.filter2D(image, -1, kernel=set_kernel)
    result = np.hstack((image, dst))
    print(dst.flatten()[:50])
elif input == 3:
    # median image (non-linear filtering)
    median = cv2.medianBlur(image, 11)
    result = np.hstack((image, median))
    print(median.flatten()[:50])

cv2.imshow('miaw', result)
cv2.waitKey(0)
