# Mengubah Citra warna menjadi citra grayscale dan citra biner
import cv2

image = cv2.imread('miaw.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('./out_file/grayscaleImage_TASK_2.jpg', grayscale_image)
cv2.imwrite('./out_file/BinaryImage_TASK_2.jpg', binary_image)

cv2.imshow("Grayscale Image", grayscale_image)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
