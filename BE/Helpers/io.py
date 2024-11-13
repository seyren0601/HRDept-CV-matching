from flask import Flask
import os
from DB import db
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

STORAGE_DIRECTORY = "submitted_pdfs\\"

def save_pdf(file:FileStorage):
    file_path = get_storage_filepath(file)
    try:
        file.save(file_path)
    except:
        raise Exception("File saving exception. filepath:{file_path}")
    
def update_pdf(user_id:int, file:FileStorage):
    old_file_path = db.find_user_filepath(user_id)
    file_path = get_storage_filepath(file)
    try:
        os.remove(old_file_path)
    except Exception as e:
        raise e
    try:
        file.save(file_path)
    except:
        raise Exception("File saving exception. filepath:{file_path}")
    
def get_storage_filepath(file:FileStorage):
    return str(STORAGE_DIRECTORY + secure_filename(file.filename))
        