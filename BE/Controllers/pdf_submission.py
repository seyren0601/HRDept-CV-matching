from werkzeug.datastructures import FileStorage
from Helpers import io
from Helpers import pdf
from Helpers import model
from DB import db
import threading

def pdf_submit(user_id:int, file:FileStorage, ocp:str='IT'):
    if db.find_user(user_id):
        file_path = io.update_pdf(user_id, file)
        db.update_user(user_id, io.get_storage_filepath(file), ocp)
    else:
        file_path = io.save_pdf(file)
        db.create_user(user_id, io.get_storage_filepath(file), ocp)
    pdf_process_thread = threading.Thread(target=pdf_process, args=(user_id, file_path, ocp))
    pdf_process_thread.start()

def pdf_process(user_id, file_path, ocp):
    raw_text = pdf.extract_text_from_pdf(file_path)
    summary = model.cv_summary(raw_text)
    json = model.summary_to_json(summary, ocp)
    json = model.json_double_check(summary, json, ocp)
    db.update_summary_and_json(user_id, summary, json)