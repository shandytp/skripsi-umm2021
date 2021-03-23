import glob
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# from image_function import otsu_thresh
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola
import glob

IMG_WIDTH, IMG_HEIGHT = 224, 224
SAMPLE_PATH = 'test_dir/'

FORMAT_FILE = ('jpg', 'JPG', 'jpeg')

# for filename in os.listdir(TRAIN_PATH_YES):
#     if filename.endswith(FORMAT_FILE):

# for file in FORMAT_FILE:
#     for image_file in enumerate(glob.glob(SAMPLE_PATH)):
#         count = 0
#         image = otsu_thresh(image_file, IMG_HEIGHT, IMG_WIDTH)
#         cv2.imwrite(f'test_dir/coba{count}', image)
#         count += 1

    # FORMAT_FILE = ('jpg', 'JPG', 'jpeg')


def apply_otsu(file_dir, img_width, img_height):
    data = []
    for filename in os.listdir(file_dir):
        if filename.endswith(FORMAT_FILE):
            print(filename)
            # data.append(filename)
            # print(data)
    
        image = cv2.imread(filename, 0)
        image = cv2.resize(image, (img_width, img_height))

        binary_global = image > threshold_otsu(image)

        cv2.imwrite('test_dir/cobagan'+1, binary_global)
    # return binary_global   

apply_otsu(SAMPLE_PATH, 224, 224)