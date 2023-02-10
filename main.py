# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:08:02 2023

@author: sbeen1840
"""

from trend import Data
from flask import Flask, jsonify
import threading

data = Data()
app = Flask(__name__)


@app.route('/home', methods=['GET'])
def get_data():
    return jsonify(data.dicts) 

if __name__ == "__main__":
    
    t1 = threading.Thread(target=data.main)
    t2 = threading.Thread(target=app.run) #debug=True
    t1.start()
    t2.start()
