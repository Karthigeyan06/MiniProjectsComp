import cv2
import numpy as np

in_image = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon13.jpg")

in_imagel=in_image[0:68,0:34]
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

in_imager=in_image[0:68,34:68]
gray_imager = cv2.cvtColor(in_imager, cv2.COLOR_BGR2GRAY)
brightness=10
contrast=2.3
gray_imager=cv2.addWeighted(gray_imager,contrast,np.zeros(gray_imager.shape,gray_imager.dtype),0,brightness)
ret, binary_imager = cv2.threshold(gray_imager, 127, 255, cv2.THRESH_BINARY)
total_pixelsr = gray_imager.shape[0] * gray_imager.shape[1]
white_pixelsr = np.sum(binary_imager == 255)
black_pixelsr = np.sum(binary_imager == 0)
white_volumer = (white_pixelsr / total_pixelsr) * 100
black_volumer = (black_pixelsr / total_pixelsr) * 100
print("---Right Volume---")
print("White Volume:", white_volumer)
print("Black Volume:", black_volumer)

print("---Total Volume---")
print("White Volume:", round((white_volumer+white_volumel)/2))
print("Black Volume:", round((black_volumer+black_volumel)/2))

m=[72,73,74,75,76,77]


if (white_volumel+white_volumer)==0:
    print("---IT'S NEW MOON DAY---")

else:

    if round((white_volumel+white_volumer)/2) in m:
        print("---IT'S FULL MOON DAY---")

    elif white_volumel<white_volumer:
        print("---It's Waxing Crescent---")

    elif white_volumel>white_volumer:
        print("---It's Waning Gibbous---")

    else:
        print("---Unknown Error---")









