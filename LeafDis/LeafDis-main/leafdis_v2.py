import cv2
import numpy as np
image = cv2.imread(r"C:\Users\karth\Downloads\leaf5.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
brightness=5
contrast=2.3
image=cv2.addWeighted(image,contrast,np.zeros(image.shape,image.dtype),0,brightness)
ret, binary_imagel = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
total_pixelsl = image.shape[0] * image.shape[1]
white_pixelsl = np.sum(binary_imagel == 255)
black_pixelsl = np.sum(binary_imagel== 0)
white_volumel = (white_pixelsl / total_pixelsl) * 100
black_volumel = (black_pixelsl / total_pixelsl) * 100
print("---Left Volume---")
print("White Volume:", white_volumel)
print("Black Volume:", black_volumel)
cv2.imshow("Result", image)
cv2.waitKey()