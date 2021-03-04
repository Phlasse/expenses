import cv2
import pytesseract
import os
import numpy as np
import preprocessor as pre

root = os.getenv('PRIVATE_ROOT')
path = root+'expenses/data/'

def load_file(root, file):
    img = cv2.imread(path+'IMG-7945.jpg')
    if img is None:
        print('nah....')
    else:
        print('sick boi')
    return img

def img_preprocessing(img):

    gray = pre.get_grayscale(img)
    thresh = pre.thresholding(gray)
    opening = pre.opening(gray)
    canny = pre.canny(gray)
    dick_pics = [img, gray, thresh, opening, canny]
    return dick_pics

def museum(dick_pics, choice="all"):
    cv2.imshow('img', img)
    cv2.waitKey(0)
    """if choice != "all":
        img = dick_pics[choice]

        h, w, c = img.shape
        boxes = pytesseract.image_to_boxes(img)
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

        cv2.imshow('img', img)
        cv2.waitKey(0)
    else:
        for i in dick_pics:
            img = i
            #h, w, c = img.shape
            #boxes = pytesseract.image_to_boxes(img)
            #for b in boxes.splitlines():
            #    b = b.split(' ')
            #    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

            cv2.imshow('img', img)
            cv2.waitKey(0)"""
    return


def main():
    img = load_file(path, path)
    dick_pics = img_preprocessing(img)
    museum(dick_pics)

if __name__ == '__main__':
    main()
