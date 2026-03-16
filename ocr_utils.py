import pytesseract
import cv2
import numpy as np
from PIL import Image

def extract_text(image):

    img = Image.open(image)
    img = np.array(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(thresh)

    return text
