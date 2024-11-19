import cv2 
img = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon13.jpg")  
crop = img[0:68, 0:34]
cv2.imshow("crop",crop)
cv2.waitKey()