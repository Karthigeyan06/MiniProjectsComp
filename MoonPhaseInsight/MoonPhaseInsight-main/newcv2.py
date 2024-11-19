import cv2
import numpy as np
key=75
in_image = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon13.jpg")
k_image=cv2.imread(r"C:\Users\karth\Downloads\full moon.jpg")
in_image=in_image[0:68,34:68]
gray_image = cv2.cvtColor(in_image, cv2.COLOR_BGR2GRAY)
brightness=10
contrast=2.3
gray_image=cv2.addWeighted(gray_image,contrast,np.zeros(gray_image.shape,gray_image.dtype),0,brightness)
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
total_pixels = gray_image.shape[0] * gray_image.shape[1]
white_pixels = np.sum(binary_image == 255)
black_pixels = np.sum(binary_image == 0)
white_volume = (white_pixels / total_pixels) * 100
black_volume = (black_pixels / total_pixels) * 100
print("White Volume:", white_volume)
print("Black Volume:", black_volume)
cv2.imshow("img", in_image)
cv2.waitKey()