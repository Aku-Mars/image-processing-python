# Menampilkan citra
import cv2

image = cv2.imread('haerin.jpg')

cv2.imshow("haerin", image)
cv2.waitKey()
