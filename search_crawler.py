# -*- coding: utf-8 -*-

from parsers.search.search_count_parser import SearchCountParser
from downloader.html_downloader import HtmlDownloader
from json_io.json_saver import JsonSaver
from parsers.search.search_page_parser import SearchPageParser


def parse_component(base_url, save_path, type):
    print("parse type: %s" % type)
    items = []

    url = base_url + '1'
    print("download url: %s" % url)
    html = HtmlDownloader.download_page(url)
    count_pages = SearchCountParser.parse(html)

    search_items = SearchPageParser.parse(html, type)
    items.extend(search_items)

    for i in range(2, count_pages + 1):
        url = base_url + str(i)
        print("download url: %s" % url)
        html = HtmlDownloader.download_page(url)
        search_items = SearchPageParser.parse(html, type)
        items.extend(search_items)

    print("save items type: %s" % type)
    JsonSaver.save(save_path, items)


def main():
    components = [
        ('https://topcomputer.ru/catalog/87/?PAGEN_1=', 'data/search/work_office.json', 'work_office'),
        ('https://topcomputer.ru/catalog/85/?PAGEN_1=', 'data/search/home.json', 'home'),
        ('https://topcomputer.ru/catalog/86/?PAGEN_1=', 'data/search/games.json', 'games'),
    ]

    for (url, path, type) in components:
        parse_component(url, path, type)


if __name__ == '__main__':
    print("Start parse search...")
    main()
