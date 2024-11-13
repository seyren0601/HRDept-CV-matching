from werkzeug.datastructures import FileStorage
from Helpers import io
from DB import db

def pdf_submit(user_id:int, file:FileStorage, ocp:str='IT'):
    if db.find_user(user_id):
        io.update_pdf(user_id, file)
        db.update_user(user_id, io.get_storage_filepath(file), ocp)
    else:
        io.save_pdf(file)
        db.create_user(user_id, io.get_storage_filepath(file), ocp)