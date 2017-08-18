import uuid

from bs4 import BeautifulSoup

from models.search_item import SearchItem


class SearchPageParser:
    @staticmethod
    def parse(html, type):
        parse_result = []

        soup = BeautifulSoup(html, 'lxml')
        ads = soup.find('div', class_='goodsList catalogItems').find_all('div', class_='item')
        for ad in ads:
            id = str(uuid.uuid4())
            try:
                title = ad.find('a', class_='name').get('title')
            except:
                title = ''
            try:
                url = 'https://topcomputer.ru' + ad.find('a', class_='name').get('href')
            except:
                url = ''
            try:
                prices = ad.find('span', class_='price').get_text()
                price = prices.split(" ")
                price = price[0]+price[1]
            except:
                price = ''

            item = SearchItem(id, url, title, price, type)
            parse_result.append(item)

        return parse_result
