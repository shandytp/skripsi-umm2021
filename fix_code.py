import cv2
import os
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola
import matplotlib.pyplot as plt
import numpy as np

DATA_PATH = 'path/to/file'

base_dir = 'path/to/file'
train = os.path.join(base_dir, DATA_PATH)
segmented_dir = os.path.join(base_dir, 'path/to/file')

for r, d, f in os.walk(train):
    for file in f:
        if ".jpg" or '.jpeg' or '.JPG' in file:
            
            imagePath = os.path.join(r, file)
            
            image = cv2.imread(imagePath, 0)
            image = cv2.resize(image, (224,224))
            thresh_niblack = threshold_niblack(image, window_size=25, k=0.8)
            thresh_niblack = cv2.ximgproc.niBlackThreshold(image, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=2*11+1, k=-0.2, binarizationMethod=cv2.ximgproc.BINARIZATION_NICK)

            binary_niblack = image > thresh_niblack
            
            '''
            Otsu Thresholding
            '''
            # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            
            cv2.imwrite(filename = os.path.join(segmented_dir, file), img=np.float32(binary_niblack))


