from bs4 import BeautifulSoup


class SearchCountParser:
    @staticmethod
    def parse(html):
        soup = BeautifulSoup(html, 'lxml')
        try:
            pages = soup.find('div', class_='items').find_all('a')[-1].get('href')
            total_pages = pages.split("=")[1]
        except:
            total_pages = 1

        return int(total_pages)
