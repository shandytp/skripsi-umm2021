import glob
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib
from image_function import otsu_thresh, sauvola_thresh, niblack_thresh

matplotlib.rcParams['font.size'] = 9

TRAIN_PATH_YES = 'brain_tumor_output/train/yes/'

FORMAT_FILE = ('jpg', 'JPG', 'jpeg')
data = []

for filename in os.listdir(TRAIN_PATH_YES):
    if filename.endswith(FORMAT_FILE):
        print(filename)
        data.append(filename)
    
    ## tinggal gabungin, jadi setelah dapet file nya bakal di apply function terus di cv2.imwrite ? 
print(len(data))