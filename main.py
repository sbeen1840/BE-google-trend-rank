# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:08:02 2023

@author: sbeen1840
"""

from trend import Data
from flask import Flask, jsonify
import threading

csv1 = "C:/Users/user/Desktop/swa-java-2023/팀프로젝트/keyword_language.csv"
csv2 = "C:/Users/user/Desktop/swa-java-2023/팀프로젝트/keyword_jobgroup.csv"
csv3 = "C:/Users/user/Desktop/swa-java-2023/팀프로젝트/keyword_academy.csv"

data1 = Data(csv1)
data2 = Data(csv2)
data3 = Data(csv3)
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/home', methods=['GET'])
def get_data():
    datas = {"프로그래밍언어":data1.dicts, "개발직군":data2.dicts, "개발교육":data3.dicts}
    return jsonify(datas)


if __name__ == "__main__":
    
    t1 = threading.Thread(target=data1.main)
    t2 = threading.Thread(target=data2.main)
    t3 = threading.Thread(target=data3.main)
    t4 = threading.Thread(target=app.run)# bug=True
    t1.start()
    t2.start()
    t3.start()
    t4.start()