import requests
from bs4 import BeautifulSoup
import sys,time
sys.stdout.reconfigure(encoding='utf-8')

response = requests.get('https://tw.stock.yahoo.com/class-quote?sectorId=46&exchange=TAI')
soup = BeautifulSoup(response.text,'lxml')

date = soup.find('time').get('datatime')
#print(date)
rows = soup.find_all('div',{'class':'Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)'})
result = []
for row in rows:
    comapny = row.find('div',{'class':'Lh(20px) Fw(600) Fz(16px) Ell'}).getText()
    price = row.find('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'}).getText()
    status_element = row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[0]
    status_class = status_element.find('span').get('class')
    status = ''
    if 'C($c-trend-down)' in status_class:
        status = '▼' + status_element.getText()
    elif 'C($c-trend-up)' in status_class:
        status = '▲' + status_element.getText()
    else:
        status = status_element.getText()

    percentage_element = row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[1]
    percentage_class = percentage_element.find('span').get('class')
    percentage = ''
    if 'C($c-trend-down)' in percentage_class:
        percentage = '▼' + percentage_element.getText()
    elif 'C($c-trend-up)' in percentage_class:
        percentage = '▲' + percentage_element.getText()
    else:
        percentage = percentage_element.getText()

    result.append([date,comapny,price,status,percentage])
print(result)
    