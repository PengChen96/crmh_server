
from flask_app import app
from flask import send_file,request,jsonify

@app.route('/uploadPage')
def uploadPage():
    return send_file('../pTest/toolsTest/html/uploadImgFile.html')
    # return "hello"

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files["imgFile"]
    file.save('E:/PyCharm/workspace/crmh_server/pTest/uploads/b.jpg')
    # file.save(os.path.join('uploads',"c.jpg"))
    return jsonify({'type':True})
