import cv2
import numpy as np
image = cv2.imread(r"C:\Users\karth\Downloads\if_leaf4.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_white = np.array([0, 0, 200], dtype=np.uint8)
upper_white = np.array([255, 30, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_white, upper_white)
mask_inv = cv2.bitwise_not(mask)
result = cv2.bitwise_and(image, image, mask=mask_inv)
total_pixelsl = image.shape[0] * image.shape[1]
white_pixelsl = np.sum(image == 255)
black_pixelsl = np.sum(image== 0)
white_volumel = (white_pixelsl / total_pixelsl) * 100


print("White Volume:", white_volumel)

cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()