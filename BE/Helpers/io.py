from flask import Flask
import sys
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

STORAGE_DIRECTORY = "submitted_pdfs\\"

def save_pdf(file:FileStorage):
    try:
        # file_path = str(STORAGE_DIRECTORY + secure_filename(file.filename))
        file.save(f"submitted_pdfs\{secure_filename(file.filename)}")
    except:
        raise Exception("File saving exception")