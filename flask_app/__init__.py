
from flask import Flask
app = Flask(__name__)

from app.controller.index.index import *
from pTest.pTestRouter import *