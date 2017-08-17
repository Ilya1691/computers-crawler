from bs4 import BeautifulSoup
from models.product_item import ProductItem
from .product_dict import ProductDicts


class ProductParser:
    base_characteristic = ProductDicts.base_characteristic
    product_characteristics = ProductDicts.product_characteristics

    def parse(self, html, search_item):
        soup = BeautifulSoup(html, "lxml")

        product_items = soup.find_all('div', {'class': 'b-product-list__item'})

        base_ch = {}
        product_ch = {}

        for item in product_items:
            name = item.find('div', {'class': 'b-product-list__val'}).text
            value = item.find('div', {'class': 'b-product-list__prop'}).text

            if name in self.base_characteristic:
                param_name = self.base_characteristic[name]
                base_ch[param_name] = value
            if name in self.product_characteristics:
                param_name = self.product_characteristics[name]
                product_ch[param_name] = value

        try:
            brand = base_ch['brand']
        except:
            brand = ''

        try:
            model = base_ch['model']
        except:
            model = ''

        product = ProductItem(
            id=search_item.id,
            url=search_item.url,
            rating=search_item.rating,
            name=search_item.name,
            price=search_item.price,
            type=search_item.type,
            brand=brand,
            model=model,
            characteristics=product_ch
        )

        return product
