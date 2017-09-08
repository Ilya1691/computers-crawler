from bs4 import BeautifulSoup
from models.product_item import ProductItem
from .product_dict import ProductDicts


class ProductParser:
    product_characteristics = ProductDicts.product_characteristics

    def parse(self, html, search_item):
        soup = BeautifulSoup(html, "lxml")
        a = []
        table = soup.find('table', class_='table_good_properties')
        product_ch = {}

        for row in table.find_all({'tr'}):
            col = row.find_all({'td'})

            if len(col) != 2:
                continue
            name = col[0].text.strip()
            value = col[1].text.strip()


            if name in self.product_characteristics:
                if name == "Форм-фактор:":
                    a.append(value)
                    param_name = self.product_characteristics[name]
                    product_ch[param_name] = a[0]
                if name != "Форм-фактор:":
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
