import os, cv2
# import pandas as pd
from PIL import Image
import pytesseract
# from StringIO import StringIO

class OCR:
    def __init__(self, img, args, size=512 ):

        self._img = img
        self._args = args
        self._size = size
        self._kernel_size = 5
        
    def process(self):
        
        # image modification
        gray = cv2.cvtColor(self._img, cv2.COLOR_RGB2GRAY)
#         binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        img_edited = cv2.medianBlur(gray, ksize=self._kernel_size)
        
        cv2.imwrite(self._args.fp_edit,img_edited)
        # pytesseract
        res_data = pytesseract.image_to_data(Image.open(self._args.fp_edit),lang='eng',output_type='data.frame') # numpy array 읽지못하고 파일을 읽으므로, os로 파일을 불러야함 , # 숫자는 lang = None
        tmp_1 = res_data.dropna()
        tmp_2 = tmp_1[tmp_1.text!=' ']
        res = ' '.join(tmp_2.text)

        return res
