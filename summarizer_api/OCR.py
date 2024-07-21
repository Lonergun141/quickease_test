import easyocr
import os

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext('test_folder\image_2.png')

print(" ".join([word for bbox, word, conf in result]))


