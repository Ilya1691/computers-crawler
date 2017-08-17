import requests


class HtmlDownloader:
    @staticmethod
    def download_page(url):
        r = requests.get(url)
        return r.text
