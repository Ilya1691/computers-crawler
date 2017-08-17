import uuid

from bs4 import BeautifulSoup

from models.search_item import SearchItem


class SearchPageParser:
    @staticmethod
    def parse(html, type):
        parse_result = []

        soup = BeautifulSoup(html, 'lxml')
        ads = soup.find('div', class_='b-catalogue').find_all('div', class_='b-what-looked__item')
        for ad in ads:
            id = str(uuid.uuid4())
            try:
                title = ad.find('a', class_='js-gtm-product-click').get('data-gtm-eventproductname')
            except:
                title = ''
            try:
                url = 'https://m.ulmart.ru' + ad.find('a', class_='js-gtm-product-click').get('href')
            except:
                url = ''
            try:
                price = ad.find('a', class_='js-gtm-product-click').get('data-gtm-eventproductprice')
            except:
                price = ''
            try:
                reiting = ad.find('span', class_='b-rating__counter').text
            except:
                reiting = ''

            item = SearchItem(id, url, reiting, title, price, type)
            parse_result.append(item)

        return parse_result
