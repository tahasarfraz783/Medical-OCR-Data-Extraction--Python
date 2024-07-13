from pdf2image import convert_from_path
import pytesseract
import numpy as np
import cv2
from PIL import Image
import re

def preprocess_image(img):
    grayscaled_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(grayscaled_img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    processsed_img = cv2.adaptiveThreshold(resized_img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,61, 20)
    return processsed_img