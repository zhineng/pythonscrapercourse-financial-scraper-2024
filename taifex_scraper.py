import requests
import json
import sys,time
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://mis.taifex.com.tw/futures/api/getQuoteList'

payload = {
           "MarketType":"0",
           "SymbolType":"F",
           "KindID":"1",
           "CID":"TXF",
           "ExpireMonth":"",
           "RowSize":"全部",
           "PageNo":"",
           "SortColumn":"",
           "AscDesc":"A"
           }

headers = {
    'Content-Type':'application/json',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

}

response = requests.post(url,data=json.dumps(payload),headers=headers)
print(response.json()['RtData']['QuoteList'])