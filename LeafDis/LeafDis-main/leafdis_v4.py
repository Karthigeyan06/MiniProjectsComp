import cv2
import numpy as np
image = cv2.imread(r"C:\Users\karth\Downloads\leaf3.png")


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_white = np.array([0, 0, 200], dtype=np.uint8)
upper_white = np.array([255, 30, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_white, upper_white)
mask_inv = cv2.bitwise_not(mask)
result = cv2.bitwise_and(image, image, mask=mask_inv)
total_pixels = image.shape[0] * image.shape[1]
white_pixels = np.sum(image == 255)

white_volume = (white_pixels / total_pixels) * 100

green_lower = np.array([40, 40, 40])
green_upper = np.array([70, 255, 255])

brown_lower = np.array([10, 100, 20])
brown_upper = np.array([20, 255, 200])

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

red_lower1 = np.array([0, 100, 100])
red_upper1 = np.array([10, 255, 255])
red_lower2 = np.array([170, 100, 100])
red_upper2 = np.array([180, 255, 255])

green_mask = cv2.inRange(hsv, green_lower, green_upper)
brown_mask = cv2.inRange(hsv, brown_lower, brown_upper)
yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
red_mask = cv2.bitwise_or(red_mask1, red_mask2)


green_pixels = cv2.countNonZero(green_mask)
brown_pixels = cv2.countNonZero(brown_mask)
yellow_pixels = cv2.countNonZero(yellow_mask)
red_pixels = cv2.countNonZero(red_mask)

print("Green pixels:", green_pixels)
print("Brown pixels:", brown_pixels)
print("Yellow pixels:", yellow_pixels)
print("Red pixels:", red_pixels)
print("White pixels", white_pixels)
print("Total pixels:", total_pixels)


val=brown_pixels+yellow_pixels+red_pixels
cal=brown_pixels+yellow_pixels+red_pixels+green_pixels
ans=round((val/cal)*100)
print(ans)
if ans<=5:
    print("---The Leaf is Healthy---")
elif ans<=20:
    print("---The Leaf is infected slightly---")

elif ans>21:
    print("---The leaf is infected---")

else:
    print("***Unknown Error***")

