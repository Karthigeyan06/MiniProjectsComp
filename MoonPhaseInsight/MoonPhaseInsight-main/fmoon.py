import cv2
import numpy as np
in_image = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon13.jpg")
k_image=cv2.imread(r"C:\Users\karth\Downloads\full moon.jpg")
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

gray_image2 = cv2.cvtColor(k_image, cv2.COLOR_BGR2GRAY)
gray_image2=cv2.addWeighted(gray_image2,contrast,np.zeros(gray_image2.shape,gray_image2.dtype),0,brightness)
ret, binary_image2 = cv2.threshold(gray_image2, 127, 255, cv2.THRESH_BINARY)
total_pixels2 = gray_image2.shape[0] * gray_image2.shape[1]
white_pixels2 = np.sum(binary_image2 == 255)
black_pixels2 = np.sum(binary_image2 == 0)

white_volume2 = (white_pixels2 / total_pixels2) * 100
black_volume2 = (black_pixels2 / total_pixels2) * 100
print("White Volume:", white_volume)
print("Black Volume:", black_volume)
print("White Volume:", white_volume2)
print("Black Volume:", black_volume2)






