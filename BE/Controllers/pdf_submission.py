from werkzeug.datastructures import FileStorage
from Helpers import io
from DB import db

def pdf_submit(user_id:int, file:FileStorage, ocp:str='IT'):
    io.save_pdf(file)
    if db.find_user(user_id):
        db.update_user(user_id, io.STORAGE_DIRECTORY + file.filename, ocp)
    else:
        db.create_user(user_id, io.STORAGE_DIRECTORY + file.filename, ocp)