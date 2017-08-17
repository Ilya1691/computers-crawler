from json_io.search_item_loader import SearchItemLoader
from parsers.product.product_parser import ProductParser
from downloader.html_downloader import HtmlDownloader
from json_io.json_saver import JsonSaver


def parse_product(item):
    url = item.url
    html = HtmlDownloader.download_page(url)
    print('download url: %s' % url)

    parser = ProductParser()
    return parser.parse(html, item)


def main():
    search_items = [
        ('data/search/motherboards.json', 'data/product/motherboards.json'),
        ('data/search/cpu.json', 'data/product/cpu.json'),
        ('data/search/memory_for_pc.json', 'data/product/memory_for_pc.json'),
        ('data/search/videocards.json', 'data/product/videocards.json'),
        ('data/search/cases_pc.json', 'data/product/cases_pc.json'),
        ('data/search/hdd.json', 'data/product/hdd.json'),
        ('data/search/power_supply.json', 'data/product/power_supply.json'),
        ('data/search/drive_pc.json', 'data/product/drive_pc.json')
    ]

    for (search_path, product_path) in search_items:
        print("load items: %s" % search_path)
        items = SearchItemLoader.load(search_path)

        product_items = []

        for item in items:
            product_item = parse_product(item)
            product_items.append(product_item)

        print("load products: %s" % product_path)
        JsonSaver.save(product_path, product_items)

if __name__ == '__main__':
    print("Start parse products...")
    main()
