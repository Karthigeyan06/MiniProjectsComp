import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r"C:\Users\karth\Downloads\if_leaf2.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=cv2.equalizeHist(image)



plt.subplot(1, 1, 1)
total_pixelsl = image.shape[0] * image.shape[1]
white_pixelsl = np.sum(image == 255)
black_pixelsl = np.sum(image== 0)
white_volumel = (white_pixelsl / total_pixelsl) * 100
black_volumel = (black_pixelsl / total_pixelsl) * 100
print("---Left Volume---")
print("White Volume:", white_volumel)
print("Black Volume:", black_volumel)


cv2.imshow("Result", image)
cv2.waitKey()
