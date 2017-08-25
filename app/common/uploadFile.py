
import os,time
from initApp import app
from flask import send_file,request,jsonify
from tools.utils.c_path import getProjectPath
from tools.log.logger import Logger
# 日志  DEBUG < INFO < WARNING < ERROR < CRITICAL
logger = Logger(logname='info.log', pyName="app.common.uploadFile.py").getlog()

ALLOWED_EXTENSIONS = ('ico', 'png', 'jpg', 'jpeg', 'gif')
# app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024      # 最大允许 2MB 文件

@app.route('/uploadPage')
def uploadPage():
    return send_file('pTest/appTest/common/uploadFile.html')
    # return "hello"

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files["imgFile"]
    isAllow = isFileAllow(file.filename)
    if not isAllow :
        response = {'type':False,'msg':"文件格式不允许"}
        logger.warning("someone wanna to submit %s format"%(file.filename))
        return jsonify(response)
    Y = time.strftime("%Y", time.localtime())
    M = time.strftime("%m", time.localtime())
    D = time.strftime("%d", time.localtime())
    T = time.strftime("%H%M%S", time.localtime())
    savePath = os.path.join(getProjectPath(),"static","pDownload","images",Y,M,D)
    # 是否存在该目录
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    filePath = os.path.join(savePath,file.filename)
    i = 0
    # 是否存在该文件
    while os.path.exists(filePath):
        gfileName = getGroupFileName(file.filename,"_pc%s_%s"%(i,T))
        filePath = os.path.join(savePath,gfileName)
        i += 1
    try:
        # 保存文件
        file.save(filePath)
        logger.info(filePath)       # log
        # fileUrl = ("http://127.0.0.1:8080/static/pDownload/images/%s/%s/%s/%s" % (Y,M,D,gfileName) )
        fileUrl = "http://p0.so.qhmsg.com/t011712ac52b3515cbf.jpg"
        response = {'type':True,'msg':"文件上传成功",'fileUrl':fileUrl}
    except:
        response = {'type':False,'msg':"文件上传失败"}
    return jsonify(response)

# 判断文件格式是否允许  在列表中为True(表示允许)
def isFileAllow(filename):
    fileSuffix = filename.split(".")[-1]
    if fileSuffix in ALLOWED_EXTENSIONS:
        return True
    return False
# 获取组合文件名
def getGroupFileName(filename,content):
    filenameList = filename.split(".")
    prefix = filenameList[-2]
    suffix = filenameList[-1]
    groupFileName = ("%s%s.%s"%(prefix,content,suffix))
    # print(groupFileName)
    return groupFileName