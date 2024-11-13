from Helpers import model
from DB import db

def get_summary(user_id:int):
    summary = db.find_summary(user_id)
    return summary

def get_json(user_id:int):
    json = db.find_summary_json(user_id)
    return json