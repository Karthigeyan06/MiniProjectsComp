import cv2
import numpy as np
from collections import Counter

# Read the image
image = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon14.jpg")

# Get the dimensions of the image
height, width, _ = image.shape

# Split the image into left and right halves
left_half = image[:, :width//2]

# Convert the left half to HSV color space
left_half_hsv = cv2.cvtColor(left_half, cv2.COLOR_BGR2HSV)

# Calculate the color distribution in the left half
wp=np.sum(left_half_hsv==80)
print(wp)
