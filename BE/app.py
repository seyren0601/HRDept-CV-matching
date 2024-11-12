from flask import Flask
from flask import request
from flask import Response
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World<h1>"

@app.route("/pdf", methods=['POST'])
def pdf_submit():
    f = request.files['pdf_file']
    f.save(f"submitted_pdfs\{secure_filename(f.filename)}")
    return Response(status=200)