import glob
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# from image_function import otsu_thresh
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola
import glob

SAMPLE_PATH = 'test_dir/'

IMG_WIDTH, IMG_HEIGHT = 224, 224

for file in enumerate(glob.glob(SAMPLE_PATH)):
    count = 0
    image = cv2.imread(file, 0)
    image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))

    # binary_global = image > threshold_otsu(image)

    cv2.imwrite(f'test_dir/coba{count}', image)
    count += 1 


