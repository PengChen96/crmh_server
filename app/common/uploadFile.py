
import os,datetime
from initApp import app
from flask import send_file,request,jsonify
from tools.utils.c_path import getProjectPath

@app.route('/uploadPage')
def uploadPage():
    return send_file('pTest/toolsTest/html/uploadImgFile.html')
    # return "hello"

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files["imgFile"]
    today = str(datetime.date.today())   # 年-月-日
    savePath = os.path.join(getProjectPath(), "pDownload", "images",today)
    # 是否存在该目录
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    filePath = os.path.join(savePath,file.filename)
    i = 0
    # 是否存在该文件
    while os.path.exists(filePath):
        fileName = "pc00"+ str(i) + file.filename
        filePath = os.path.join(savePath,fileName)
        i += 1
    # 保存文件
    file.save(filePath)
    return jsonify({'type':True})
