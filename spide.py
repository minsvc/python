import requests
from bs4 import BeautifulSoup

post_url='http://192.168.30.57/zabbix/index.php'
post_data={'request':'hosts.php?ddreset=1','name':'Admin','password':'zabbix','autologin':'1','enter':'Sign in'}
#headers={'Content-Length': '84', 'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'DNT': '1', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1', 'Host': '192.168.30.57', 'Referer': 'http://192.168.30.57/zabbix/index.php?request=hosts.php%3Fddreset%3D1', 'Cache-Control': 'max-age=0', 'Content-Type': 'application/x-www-form-urlencoded'}

headers={}
session=requests.session()
content=session.post(post_url,headers=headers,data=post_data)
url='http://192.168.30.57/zabbix/users.php?ddreset=1'
r=session.get(url)
print(r.headers)
soup=BeautifulSoup(r.text)
print(soup.prettify())

