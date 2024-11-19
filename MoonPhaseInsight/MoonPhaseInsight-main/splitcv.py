import cv2
import numpy as np
in_image = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon14.jpg")
height, width, channels=in_image.shape
nwidth=width//2
left_half=in_image[:,:nwidth]
right_half=in_image[:,nwidth:]
tp1= left_half.shape[0] * left_half.shape[1]
tp2=right_half.shape[0] * right_half.shape[1]
wp1=np.sum(left_half==255)
bp1=np.sum(left_half==0)
wp2=np.sum(right_half==255)
bp2=np.sum(right_half==0)
wv1=(wp1/tp1)*100
bv1=(bp1/tp1)*100
wv2=(wp2/tp2)*100
bv2=(bp2/tp2)*100
print(wp1)
print("Left Half: \n White volume:", wv1, "\n Black volume:", bv1)
print("Right Half: \n White volume:", wv2, "\n Black volume:", bv2)
cv2.imshow("left",left_half)
cv2.imshow("right",right_half)
cv2.waitKey(0)

