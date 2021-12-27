import requests
# 忽略警告
from requests.packages import urllib3
urllib3.disable_warnings()

url = 'https://ssr2.scrape.center/'
# verify参数控制是否验证证书
request = requests.get(url=url, verify=False)
print(request.status_code)