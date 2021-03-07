import cv2
import pytesseract
import os
import numpy as np
import expenses.preprocessor as pre

def thresh_pipeline(img, detail_print = False):
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    if detail_print == True:
        for i in range(6):
            plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
            plt.show()

    return images

def grocepre(img):
    """ mit dieser Funktion kann das preprocessing angepasst werden"""
    img_prepro = pre.get_grayscale(img)
    img_prepro = pre.remove_noise(img_prepro)
    img_prepro = pre.dilate(img_prepro)
    img_prepro = pre.erode(img_prepro)
    img_prepro = pre.opening(img_prepro)
    img_prepro = pre.thresholding(img_prepro)

    return img_prepro

def grocepriterator(img):
    img_gray = pre.get_grayscale(img)
    imgages = [img_gray]
    img_prepro1 = pre.thresholding(img_gray)

    img_prepro2 = pre.remove_noise(img_gray)
    img_prepro2 = pre.thresholding(img_prepro2)

    img_prepro3 = pre.remove_noise(img_gray)
    img_prepro3 = pre.opening(img_prepro3)
    img_prepro3 = pre.thresholding(img_prepro3)

    img_prepro4 = pre.remove_noise(img_gray)
    img_prepro4 = pre.opening(img_prepro4)

    imgages.append(img_prepro1)
    imgages.append(img_prepro2)
    imgages.append(img_prepro3)
    imgages.append(img_prepro4)
    imgages.append(grocepre(img))

    return imgages

def plot_n_box(img_prepro):
    """ Mit dieser Funktion kann das Bild und die Character-Identifikation betrachtet werden"""
    print(img_prepro)
    h, w= img_prepro.shape
    boxes = pytesseract.image_to_boxes(img_prepro)
    for b in boxes.splitlines():
        b = b.split(' ')
        img_prepro = cv2.rectangle(img_prepro, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    cv2.imshow('img', img_prepro)
    cv2.waitKey(0)

    return

def img_to_str(img):
    """Hier wird das preprocessierte Bild zum string verarbeitet"""
    # Adding custom options
    #custom_config = r'--oem 3 --psm 6'
    result = pytesseract.image_to_string(img)#, config=custom_config)

    return result

def pipeline(img,pipe_select = 0):
    #img_prepro = grocepre(img)
    #plot_n_box(img_prepro)
    images = thresh_pipeline(img)
    images.extend(grocepriterator(img))
    img_strings = [img_to_str(x).lower() for x in images]

    return img_strings
