import cv2
import os
import numpy as np
import expenses.img_preprocessor as pre
import expenses.img_postprocessor as post

root = os.getenv('PRIVATE_ROOT')
path = root+'expenses/data/'
files = ['IMG-7945.jpg','IMG-7941.jpg']

def load_file(path, file):
    img = cv2.imread(path+file)
    return img

def main():
    img = load_file(path, files[0])
    print("Image was loaded")
    pre_imgs = pre.pipeline(img)
    print("Image has been prepocessed in several ways")
    haul = post.identify(pre_imgs)
    print(haul)

    return

if __name__ == '__main__':
    main()
