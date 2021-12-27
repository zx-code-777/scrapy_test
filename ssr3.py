import requests

url = 'https://ssr3.scrape.center/'
r = requests.get(url=url, auth=('admin', 'admin'))
print(r.status_code)
