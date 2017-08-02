
from flask import Flask
app = Flask(__name__)

from pTest.appTest.pTestRouter import *
from app.controller.index.index import *

