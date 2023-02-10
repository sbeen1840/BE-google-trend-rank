# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:08:02 2023

@author: sbeen1840
"""

import sys
import time
import csv
import json
import pandas as pd
from pytrends.request import TrendReq

#%%
class Data:
    def __init__(self):

        # 사용자 맞춤 변수 지정
        self.numb = 2 # 상위부터 추출 개수 
        self.lang = 'ko' # pytrend 기준 언어 설정
        self.time = 540 # pytrend 기준 시간대 설정
        self.geo = 'KR' # pytrend 기준 위치 설정
        self.month = 1 # 현재부터 n개월간의 기록 (정수만 입력)
        self.update = 1 # 업데이트할 주기(단위 sec)  # 86400 하루
        self.address = "C:/Users/sbeen/OneDrive/바탕 화면/keyword_data.csv"
        self.dicts = 7 # 웹에 띄워지는 초기값
        # self.jsons = 0


    def read_csv(self):
        self.lines = [] # 유사키워드별 리스트 분류
        self.keys = [] # 유사키워드 중 대표 키워드만 모음
        with open(self.address, "r") as file:
            reader = csv.reader(file)
            for line in reader:
                line = [field for field in line if field != ''] # 최대 5개 입력인데, 미만일 경우 발생하는 공백제거
                self.lines.append(line) # 한 줄에 해당하는 유사키워드별로 묶기
                if line:
                    self.keys.append(line[0]) # 맨 첫 번째를 대표키워드로 지정
                    
    def py_trends(self):
        self.sums = [] # 키워드에 대한 총 합산 값
        pytrends = TrendReq(hl=self.lang, tz=self.time) # pytrend 언어, 시간대 설정
        for i in range(len(self.lines)): # 키워드별 pytrend 데이터 수집 반복
            pytrends.build_payload(self.lines[i], cat=0, timeframe='today %d-m'%self.month, geo=self.geo) # 최신 3달치
            data = pytrends.interest_over_time() 
            data = data.reset_index() 
            data = data.iloc[:, 1:-1] # 필요없는 부분 date_time 열 제거
            self.sums.append(int(data.sum().sum())) # 유사키워드 모두 합한 값
                    

    def to_json(self):
        # dicts = dict(zip(self.keys, self.sums)) # list 두 개를 각각 key, value로 
        
        df = pd.DataFrame({'keys': self.keys, 'sums': self.sums})
        print('\n유사키워드에 대한 검색량 총합 :\n', df)
        df = df.sort_values(by='sums', ascending=False) # 내림차순
        print('\n키워드별 정렬:\n', df)
        df = df[:self.numb]
        print('\n상위 n개 추출:\n', df)
        df = df.set_index('keys').T 
        self.dicts = df.to_dict('records')[0] #orient = 'records'임
        print('\nGET에 사용될 정보 :', self.dicts)
        self.jsons = json.dumps(self.dicts) # dict -> json
        return self.jsons # get_data에서 참조하는 값 즉 data.jsons
    

    def main(self):
        try:
            while True:
                print("2. reading csv file\n")
                self.read_csv()
                print("3. loading a google trend data\n")
                self.py_trends()
                print("4. making a json file")
                print('\nJson으로 변경된 정보: ', self.to_json(),'\n')
                print("5. waiting.. It takes a day to update the pytrend data\n\n\n")
                time.sleep(self.update)
                print("1. program restart!\n")
        except KeyboardInterrupt:
                print("Program interrupted by user.")
                sys.exit(0)
