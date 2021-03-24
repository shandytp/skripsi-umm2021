import cv2
import os
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola
import matplotlib.pyplot as plt
import numpy as np

DATA_PATH = 'brain_tumor_output/val/yes/'

base_dir = 'D:/Kuliah baru/SMT 8/Coding Skripsi'
train = os.path.join(base_dir, DATA_PATH)
segmented_dir = os.path.join(base_dir, 'brain_tumor_fix/sauvola/val/yes')

for r, d, f in os.walk(train):
    for file in f:
        if ".jpg" or '.jpeg' or '.JPG' in file:
            
            imagePath = os.path.join(r, file)
            
            image = cv2.imread(imagePath, 0)
            image = cv2.resize(image, (224,224))

            res = image.copy()
            '''
            Sauvola Thresholding
            '''
            thresh_sauvola = threshold_sauvola(image, window_size=25)
            thresh_sauvola = cv2.ximgproc.niBlackThreshold(image, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=2*11+1, k=-0.2, binarizationMethod=cv2.ximgproc.BINARIZATION_SAUVOLA)

            binary_sauvola = image > thresh_sauvola
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    if binary_sauvola[i][j]==True:
                        res[i][j]=255
                    else:
                        res[i][j]=0

            '''
            Niblack Thresholding
            '''
            # thresh_niblack = threshold_niblack(image, window_size=25, k=0.8)
            # thresh_niblack = cv2.ximgproc.niBlackThreshold(image, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=2*11+1, k=-0.2, binarizationMethod=cv2.ximgproc.BINARIZATION_NICK)

            # binary_niblack = image > thresh_niblack
            # for i in range(res.shape[0]):
            #     for j in range(res.shape[1]):
            #         if binary_niblack[i][j]==True:
            #             res[i][j]=255
            #         else:
            #             res[i][j]=0

            # print(res)
            
            '''
            Otsu Thresholding
            '''
            # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            
            cv2.imwrite(filename = os.path.join(segmented_dir, file), img=res)


