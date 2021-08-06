import requests
from requests.cookies import RequestsCookieJar
import csv
import json
import time


def huoqushuju():
    cookie_jar = RequestsCookieJar()
    cookie_jar.set("BAIDUID", "B1CCDD4B4BC886BF99364C72C8AE1C01:FG=1", domain="baidu.com")

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'Content-Type': 'application/json',
        'Referer': 'http://183.194.241.192:8080/Search/Parking',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    params = (
        ('order', 'asc'),
        ('offset', '0'),
        ('limit', '20'),
    )
    response = requests.get('http://183.194.241.192:8080/Search/SearchGarage', headers=headers, params=params,
                            cookies=cookie_jar, verify=False)

    for i in response.json()['data']:
        with open("上海市停车场数据.csv", 'a', newline='', encoding='utf-8') as f:
            wirter = csv.writer(f)
            wirter.writerow([i['GarageId'], i['GarageName'], i['GarageAddress']])


def huoqujingweidu():
    with open('上海市停车场数据.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i in reader:
            print(i)

            url = 'http://api.map.baidu.com/place/v2/search?query=' + i[2] + '&region=上海&output=json&ak=nls5UIpFa636ouk2yOMGPYg6'
            r = requests.get(url)
            r = r.json()
            zuobiao = r['results'][0]['location']

            print(zuobiao)


def main():
    huoqushuju()


if __name__ == '__main__':
    main()
