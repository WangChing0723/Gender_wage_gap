import requests
import json
import urllib

url = "https://apiservice.mol.gov.tw/OdService/download/A17000000J-030266-cZZ"
urllib.request.urlretrieve(url,"result.txt")
with open("result.txt","r",encoding="utf-8") as f:
    result = json.loads(f.read())

search = input("輸入你想查詢的年份(民國99~109): ") + "年"
n = 0
print(search)
for i in result:
    if search == i['細項']:
        print(f"{i['細項']}的兩性薪資差距比（%）為 {i['兩性差距（%）']}%")
        n += 1
if n == 0:
    print(f"未搜尋到{search}的資料")