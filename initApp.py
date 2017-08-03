
from flask import Flask
app = Flask(__name__)

# 把有route的都添加进来
from app.common.uploadFile import *
from app.controller.index.index import *