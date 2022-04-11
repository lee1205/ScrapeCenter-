import requests


class Spa1:
    def __init__(self, url):
        self.url = url


    def run(self):
        urll = self.url
        for i in urll:
            response = requests.get(i).json()
            datas = response['results']
            for data in datas:
                item = {}
                item['编号'] = data['id']
                item['名称'] = data['name']
                item['别名'] = data['alias']
                item['分类'] = data['categories']
                item['上映日期'] = data['published_at']
                item['地区'] = data['regions']
                item['时长(分钟)'] = data['minute']
                item['封面'] = data['cover']
                print(item)





if __name__ == '__main__':
    base_url = 'https://spa1.scrape.center/api/movie/?limit=10&offset={}'
    urllist = []
    for i in range(0, 10):
        url = base_url.format(i*10)
        urllist.append(url)
        spa = Spa1(urllist)
    spa.run()