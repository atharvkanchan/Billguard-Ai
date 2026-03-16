import pytesseract
import cv2
import numpy as np
from PIL import Image

def extract_text(image):

    img = np.array(Image.open(image))

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(
        gray,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,11,2
    )

    text = pytesseract.image_to_string(thresh)

    return text
