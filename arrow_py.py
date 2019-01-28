import arrow

a = arrow.utcnow()
a.timetuple()
a.timestamp
a.format("YYYY-MM-DD hh:mm:ss")

import datetime
isinstance(arrow.arrow.datetime, datetime.datetime)

arrow.Arrow(2017,11,11)

datetime.datetime(2017,11,11)

a.for_json()

import time
time.strftime()

import requests

# 爬取百度首页中文乱码解决方法
resp = requests.get('https://www.baidu.com/')
resp.content.decode("utf-8","ignore")
# 或
resp = requests.get('https://www.baidu.com/')
resp.encoding = 'utf-8'
resp.text

url = 'https://c.runoob.com/'
proxies = {
    'http':'119.101.117.254:9999',
    "https":'119.101.117.254:9999'
}
resp = requests.get(url, proxies=proxies)
resp.content

resp = requests.get('http://127.0.0.1:3002/search/get_regulatory_anomaly')
resp.json()


# download images
resp = requests.get('https://assets.readthedocs.org/sustainability/readthedocs-logo-fs8.png')
with open('fs8.png', 'wb') as f:
    f.write(resp.content)


