import cv2
import numpy as np

in_image = cv2.imread(r"C:\Users\karth\Downloads\Moon Images\moon24.jpg")

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

m=[72,73,74,75,76,77,78]

def cont():
    in_imagel1=in_image[0:34,0:34]
    in_imager1=in_image[34:68,0:34]
    gray_imagel1 = cv2.cvtColor(in_imagel1, cv2.COLOR_BGR2GRAY)
    brightness=10
    contrast=2.3
    gray_imagel1=cv2.addWeighted(gray_imagel1,contrast,np.zeros(gray_imagel1.shape,gray_imagel1.dtype),0,brightness)
    ret, binary_imagel1 = cv2.threshold(gray_imagel1, 127, 255, cv2.THRESH_BINARY)
    total_pixelsl1 = gray_imagel1.shape[0] * gray_imagel1.shape[1]
    white_pixelsl1 = np.sum(binary_imagel1 == 255)
    black_pixelsl1 = np.sum(binary_imagel1== 0)
    white_volumel1 = (white_pixelsl1 / total_pixelsl1) * 100
    black_volumel1 = (black_pixelsl1 / total_pixelsl1) * 100

    gray_imager1 = cv2.cvtColor(in_imager1, cv2.COLOR_BGR2GRAY)
    gray_imager1=cv2.addWeighted(gray_imager1,contrast,np.zeros(gray_imager1.shape,gray_imager1.dtype),0,brightness)
    ret, binary_imager1 = cv2.threshold(gray_imager1, 127, 255, cv2.THRESH_BINARY)
    total_pixelsr1 = gray_imager1.shape[0] * gray_imager1.shape[1]
    white_pixelsr1 = np.sum(binary_imager1 == 255)
    black_pixelsr1 = np.sum(binary_imager1== 0)
    white_volumer1 = (white_pixelsr1 / total_pixelsr1) * 100
    black_volumer1 = (black_pixelsr1 / total_pixelsr1) * 100
    


    in_imagel2=in_image[0:34,34:68]
    in_imager2=in_image[34:68,34:68]
    gray_imagel2 = cv2.cvtColor(in_imagel2, cv2.COLOR_BGR2GRAY)
    brightness=10
    contrast=2.3
    gray_imagel2=cv2.addWeighted(gray_imagel2,contrast,np.zeros(gray_imagel2.shape,gray_imagel2.dtype),0,brightness)
    ret, binary_imagel2 = cv2.threshold(gray_imagel2, 127, 255, cv2.THRESH_BINARY)
    total_pixelsl2 = gray_imagel2.shape[0] * gray_imagel2.shape[1]
    white_pixelsl2 = np.sum(binary_imagel2 == 255)
    black_pixelsl2 = np.sum(binary_imagel2== 0)
    white_volumel2 = (white_pixelsl2 / total_pixelsl2) * 100
    black_volumel2 = (black_pixelsl2 / total_pixelsl2) * 100

    gray_imager2 = cv2.cvtColor(in_imager2, cv2.COLOR_BGR2GRAY)
    gray_imager2=cv2.addWeighted(gray_imager2,contrast,np.zeros(gray_imager2.shape,gray_imager2.dtype),0,brightness)
    ret, binary_imager2 = cv2.threshold(gray_imager2, 127, 255, cv2.THRESH_BINARY)
    total_pixelsr2 = gray_imager2.shape[0] * gray_imager2.shape[1]
    white_pixelsr2 = np.sum(binary_imager2 == 255)
    black_pixelsr2 = np.sum(binary_imager2== 0)
    white_volumer2 = (white_pixelsr2 / total_pixelsr2) * 100
    black_volumer2 = (black_pixelsr2 / total_pixelsr2) * 100

    if (white_pixelsl1<white_pixelsl2 or white_pixelsr1==white_pixelsr2) and (white_pixelsl1==white_pixelsl2 or white_pixelsr1<white_pixelsr2) :
        sol="---It's Waxing Crescent---"
    

    else:
        sol="---It's Wanning Gibbous---"

    print(sol)

if (white_volumel+white_volumer)==0:
    print("---IT'S NEW MOON DAY---")

else:

    if round((white_volumel+white_volumer)/2) in m:
        print("---IT'S FULL MOON DAY---")

    elif white_volumel<white_volumer:
        
            cont()
            
            
    elif white_volumel>white_volumer:
        
            cont()
            

    else:
        print("---Unknown Error---")

print("***This Results may or may not be Accurate***")










