from flask import Flask
from flask import request
from flask import Response
from Controllers.pdf_submission import pdf_submit
from Controllers.llm_model import get_summary
from Controllers.llm_model import get_json
from Helpers import io
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World<h1>"

@app.route("/pdf", methods=['POST'])
def pdf():
    user_id = request.args.get('user_id', -1, type=int)
    occupation = request.args.get('ocp', "IT", type=str)
    f = request.files['pdf_file']
    
    if user_id == -1:
        return Response(response="Invalid user id", status=400)
    
    try:
        pdf_submit(user_id, f, occupation)
    except Exception as e:
        return Response(response=str(e), status=500)
    return Response(status=200)
    
@app.route("/pdf_summary", methods=['GET'])
def pdf_summary():
    user_id = request.args.get('user_id', -1, type=int)
    if user_id == -1:
        return Response(response="Invalid user id", status=400)
    summary = get_summary(user_id)
    return summary

@app.route("/pdf_json", methods=['GET'])
def pdf_json():
    user_id = request.args.get('user_id', -1, type=int)
    if user_id == -1:
        return Response(response="Invalid user id", status=400)
    json = get_json(user_id)
    return json