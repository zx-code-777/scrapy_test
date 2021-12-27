import requests
import logging
import re
from urllib.parse import urljoin

# %（acstime)s 时间
# %（filename)s 日志文件名
# %（funcName)s 调用日志的函数名
# %（levelname)s 日志的级别
# %（module)s 调用日志的模块名
# %（message)s 日志信息
# %（name)s logger的name，不写的话默认是root
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
base_url = 'https://ssr1.scrape.center'
total_page = 10


def scrape_page(url):
    logging.info('scrape %s...', url)
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = f'{base_url}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(base_url, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    drama_pattern = re.compile('<div.*?dram.*?<p.*?>(.*?)</p>', re.S)
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published = re.search(published_at_pattern, html).group(1).strip() if \
        re.search(published_at_pattern, html) else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published': published,
        'score': score,
        'drama': drama
    }

# 将数据保存为json格式的文件
import json
from os import makedirs
from os.path import exists
# 定义文件夹名为results的文件夹
results_dir = 'results'
# 如果results的文件夹不存在则创建它
exists(results_dir) or makedirs(results_dir)


def sav_data(data):
    name = data.get('name')
    data_path = f'{results_dir}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

import multiprocessing

def main(page):
        # 获取当前页页的html信息
        index_html = scrape_index(page)
        # 获取每个电影的详细页地址
        detail_urls = parse_index(index_html)
        # logging.info('detail urls %s', list(detail_urls))
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info('get detail data %s', data)
            logging.info('saving data to json file')
            sav_data(data)
            logging.info('data saved successfully')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, total_page+1)
    pool.map(main, pages)
    pool.close()
    pool.join()
