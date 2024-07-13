from pdf2image import convert_from_path
import pytesseract
import numpy as np
import cv2
from PIL import Image
import re
from backend.src.util import preprocess_image
from parser_presciption import PrescriptionParser
from parser_patient_details import PatientDetailsParser


pdf_path = (r'../documents/patient_details/pd_1.pdf')
poppler_path = r'C:\poppler-24.02.0\Library\bin'
pytesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = pytesseract_path


def extract(file_path, file_format):
    converted_pages = convert_from_path(file_path, poppler_path=poppler_path)
    document_text = ''

    for i in range(len(converted_pages)):
        converted_pages[i] = preprocess_image(converted_pages[i])

    for i in range(len(converted_pages)):
        page_content = pytesseract.image_to_string(converted_pages[i], lang='eng')
        document_text += '\n' + page_content


    if file_format == 'prescription':
        extracted_data =  PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data =  PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid Document Format: {file_format}")
    return extracted_data

if __name__ == "__main__":
    data = extract(pdf_path, 'patient_de23s')
    print(data)