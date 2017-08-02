from flask_app import app
from flask import jsonify
# from flask_cors import *      #跨域

# app = Flask(__name__)
# CORS(app, supports_credentials=True)  #跨域

@app.route('/')
def index():
    return "hello world!"
    # return send_file('unitTest.html')

data = {'a':123, 'b':456}
@app.route('/getData', methods=['GET'])
def getData():
    return jsonify(data)
#
# if __name__ == '__main__':
#     app.run(debug=True)