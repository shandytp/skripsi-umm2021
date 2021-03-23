import glob
import cv2
import os
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.size'] = 9

TRAIN_PATH_YES = 'brain_tumor_output/train/yes/'

def otsu_thresh(file, img_width, img_height):
    '''
    Konversi image menjadi binary menggunakan metode Otsu Thresholding

    Parameters
    ----------
    file: string
        Path ke file image yang kita inginkan
    
    img_width: int
        Size untuk width gambar kita
    
    img_height: int
        Size untuk height gambar kita

    Returns
    -------
    binary_global: Boolean
        masih belum tahu hehe
    '''

    image = cv2.imread(file, 0)
    image = cv2.resize(image, (img_width, img_height))

    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def niblack_thresh(file, img_width, img_height, window_size):
    '''
    Konversi image menjadi binary menggunakan metode Niblack Thresholding

    Parameters
    ----------
    file: string
        Path ke file image yang kita inginkan
    
    img_width: int
        Size untuk width gambar kita
    
    img_height: int
        Size untuk height gambar kita
    
    window_size: int
        Size untuk window

    Returns
    -------
    binary_niblack: Boolean
        masih belum tahu hehe
    '''
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (img_width, img_height))

    thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)
    thresh_niblack = cv2.ximgproc.niBlackThreshold(image, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=2*11+1, k=-0.2, binarizationMethod=cv2.ximgproc.BINARIZATION_NICK)

    binary_niblack = image > thresh_niblack

    return binary_niblack

def sauvola_thresh(file, img_width, img_height, window_size):
    '''
    Konversi image menjadi binary menggunakan metode Sauvola Thresholding

    Parameters
    ----------
    file: string
        Path ke file image yang kita inginkan
    
    img_width: int
        Size untuk width gambar kita
    
    img_height: int
        Size untuk height gambar kita
    
    window_size: int
        Size untuk window

    Returns
    -------
    binary_sauvola: Boolean
        masih belum tahu hehe
    '''
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (img_width, img_height))

    thresh_sauvola = threshold_sauvola(image, window_size=window_size)
    thresh_sauvola = cv2.ximgproc.niBlackThreshold(image, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=2*11+1, k=-0.2, binarizationMethod=cv2.ximgproc.BINARIZATION_SAUVOLA)

    binary_sauvola = image > thresh_sauvola

    return binary_sauvola

# Disini apply function ke satu file gambar

# gambar = niblack_thresh('test.jpg', 224, 224, 25)
# gambar = sauvola_thresh('test.jpg', 224, 224, 25)
gambar = otsu_thresh('test.jpg', 224, 224)
filename = 'test_otsu_baru_lagi.jpg'
cv2.imwrite(filename, gambar)
# print(gambar)


plt.imshow(gambar, cmap='gray')
plt.show()
plt.axis('off')

