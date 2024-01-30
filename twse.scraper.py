import requests
import json
import sys,time
sys.stdout.reconfigure(encoding='utf-8')

response = requests.get('https://www.twse.com.tw/rwd/zh/afterTrading/BWIBBU_d?date=20240130&selectType=30&response=json&_=1706626482582')
print(response.json()['data'])
