import os
import requests
import fitz  # PyMuPDF
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path, type='pypdf2'):
    text = ""
    if type == 'pymupdf':
        with fitz.open(file_path) as pdf:
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                text += page.get_text("text", sort=True)
    else:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    return text