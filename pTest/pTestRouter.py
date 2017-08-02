from flask_app import app
from flask import send_file

@app.route('/upload')
def upload():
    return send_file('../pTest/html/uploadImgFile.html')
    # return "hello"
