import httpx
url = 'https://spa16.scrape.center/'
client = httpx.Client(http2=True)
request = httpx.get(url=url)
print(request.text)