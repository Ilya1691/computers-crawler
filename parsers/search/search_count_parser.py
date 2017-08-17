from bs4 import BeautifulSoup


class SearchCountParser:
    @staticmethod
    def parse(html):
        soup = BeautifulSoup(html, 'lxml')
        try:
            pages = soup.find('div', class_='l-reducer') \
                .find_all('li', class_='b-paginator__item ')[-1] \
                .find_all('a', class_='b-paginator__number')[-1] \
                .get('href')
            total_pages = pages.split("=")[1]
        except:
            total_pages = 1

        return int(total_pages)
