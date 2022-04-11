import requests
from lxml import etree
from queue import Queue
import urllib3

class Ssr2:
    def __init__(self, url_que):
        self.url = url_que

    def run(self):
        while self.url.empty() == False:
            url = self.url.get()
            urllib3.disable_warnings()
            response = requests.get(url, verify=False).text
            self.parse(response)

    def parse(self, data):
        e = etree.HTML(data)
        res = e.xpath('//*[@id="index"]/div[1]/div[1]/div')
        for i in res:
            item = {}
            item['标题'] = i.xpath('div[1]/div[1]/div[2]/a/h2/text()')[0]
            item['封面'] = i.xpath('div[1]/div[1]/div[1]/a/img/@src')[0]
            item['标签'] = i.xpath('div[1]/div[1]/div[2]/div[1]/button/span/text()')[0]
            item['信息'] = i.xpath('div[1]/div[1]/div[2]/div[2]/span/text()')[0]
            # item['年份'] = e.xpath('//*[@id="index"]/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[3]/span/text()')[0]
            item['评分'] = i.xpath('div[1]/div[1]/div[3]/p[1]/text()')[0]
            print(item)


if __name__ == '__main__':
    url_que = Queue()
    base_url = 'https://ssr2.scrape.center/page/{}'
    for i in range(1, 11):
        url = base_url.format(i)
        url_que.put(url)
    ssr = Ssr2(url_que)
    ssr.run()

