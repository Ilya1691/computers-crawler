from bs4 import BeautifulSoup

from models.search_bench import SearchItem


class SearchPageParser:
    @staticmethod
    def parse(html, type):
        parse_result = []
        soup = BeautifulSoup(html, 'lxml')
        name = soup.find('table', class_='chart')

        for ad in name:
            try:
                name_product = ad.find('td', 'chart').text
            except:
                name_product = ''
            try:
                reiting = ad.find('td', 'value').text
            except:
                reiting = ''

            if name_product and reiting !='':
                item = SearchItem(name_product, reiting, type)
                parse_result.append(item)

        return parse_result
