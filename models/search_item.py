import json


class SearchItem:
    def __init__(self, id, url, name, price, type, characteristics):
        self.id = id
        self.url = url
        self.name = name
        self.price = price
        self.type = type
        self.characteristics = characteristics

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
