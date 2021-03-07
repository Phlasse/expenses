import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import pytesseract


root = os.getenv('PRIVATE_ROOT')
path = root+'expenses/data/'
files = ['IMG-7945.jpg','IMG-7941.jpg']

file = files[0]
img = cv2.imread(path+file)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

#for i in range(6):
#    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])

#plt.show()

custom_config = r'--oem 3 --psm 6'
results = []

for i in range(6):
    results.append(pytesseract.image_to_string(images[i]))# config=custom_config))
for i in results:
    print(i)
