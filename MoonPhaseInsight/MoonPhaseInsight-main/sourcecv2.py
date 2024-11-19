import cv2
import numpy as np
key=75
in_image = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon5.jpg")
k_image=cv2.imread(r"C:\Users\karth\Downloads\full moon.jpg")
in_imagel=in_image[0:68,0:68]
gray_imagel = cv2.cvtColor(in_imagel, cv2.COLOR_BGR2GRAY)
brightness=10
contrast=2.3
gray_imagel=cv2.addWeighted(gray_imagel,contrast,np.zeros(gray_imagel.shape,gray_imagel.dtype),0,brightness)
ret, binary_imagel = cv2.threshold(gray_imagel, 127, 255, cv2.THRESH_BINARY)
total_pixelsl = gray_imagel.shape[0] * gray_imagel.shape[1]
white_pixelsl = np.sum(binary_imagel == 255)
black_pixelsl = np.sum(binary_imagel== 0)
white_volumel = (white_pixelsl / total_pixelsl) * 100
black_volumel = (black_pixelsl / total_pixelsl) * 100
print("---Left Volume---")
print("White Volume:", white_volumel)
print("Black Volume:", black_volumel)