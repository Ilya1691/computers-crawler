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
        ('https://m.ulmart.ru/catalog/power_supply2?pageNum=', 'data/search/power_supply.json', 'power_supply'),
        ('https://m.ulmart.ru/catalog/cpu?pageNum=', 'data/search/cpu.json', 'cpu'),
        ('https://m.ulmart.ru/catalog/hdd?pageNum=', 'data/search/hdd.json', 'hdd'),
        ('https://m.ulmart.ru/catalog/drive_pc?pageNum=', 'data/search/drive_pc.json', 'drive_pc'),
        ('https://m.ulmart.ru/catalog/videocards?pageNum=', 'data/search/videocards.json', 'videocards'),
        ('https://m.ulmart.ru/catalog/cases_pc?', 'data/search/cases_pc.json', 'cases_pc'),
        ('https://m.ulmart.ru/catalog/motherboards?pageNum=', 'data/search/motherboards.json', 'motherboards'),
        ('https://m.ulmart.ru/catalog/memory_for_pc?pageNum=', 'data/search/memory_for_pc.json', 'memory_for_pc')
    ]

    for (url, path, type) in components:
        parse_component(url, path, type)


if __name__ == '__main__':
    print("Start parse search...")
    main()
