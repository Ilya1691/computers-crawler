from bs4 import BeautifulSoup
from models.product_item import ProductItem
from .product_dict import ProductDicts


class ProductParser:
    product_characteristics = ProductDicts.product_characteristics

    def parse(self, html, search_item):
        soup = BeautifulSoup(html, "lxml")

        product_items = soup.find_all('table', {'class': 'table_good_properties'})

        product_ch = {}

        for item in product_items:
            name = item.find('td', {'class': 'group_prop'}).text
            value = item.find('td', {'class': 'prop_name'}).text

            if name in self.product_characteristics:
                param_name = self.product_characteristics[name]
                product_ch[param_name] = value

        product = ProductItem(
            id=search_item.id,
            url=search_item.url,
            name=search_item.name,
            price=search_item.price,
            type=search_item.type,
            characteristics=product_ch
        )

        return product
