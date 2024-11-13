import pymongo
from werkzeug.datastructures import FileStorage

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongo_client['pdf_matching']
col = db['data']

def create_user(user_id:int, file_location:str, ocp:str):
    col.insert_one(
        {
            "user_id":user_id,
            "pdf_location":file_location,
            "ocp":ocp,
            "summary":"",
            "summary_json":""
        }
    )
    
def update_user(user_id:int, file_location:str, ocp:str):
    col.update_one(
        {
            "user_id":user_id
        },
        {
            "$set": {
                "pdf_location":file_location,
                "ocp":ocp
            }
        }
    )
    
def update_summary_and_json(user_id:int, summary:str, json:str):
    col.update_one(
        {
            "user_id":user_id
        },
        {
            "$set": {
                "summary":summary,
                "summary_json":json
            }
        }
    )
    
def find_user(user_id:int):
    if col.count_documents({"user_id":user_id}, limit=1) == 1:
        return True
    else:
        return False
    
def find_summary(user_id:int):
    res = col.find_one({"user_id":user_id})
    summary = res["summary"]
    return summary

def find_summary_json(user_id:int):
    res = col.find_one({"user_id":user_id})
    json = res["summary_json"]
    return json
    
def find_user_filepath(user_id:int):
    res = col.find_one({"user_id":user_id})
    pdf_path = res["pdf_location"]
    
    return pdf_path

    