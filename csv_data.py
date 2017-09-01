from json_io.search_item_loader import SearchItemLoader
import re
import csv

def write_cvs(datas):
    with open('data/System_case.cvs', 'a') as f:
        for data in datas:
            writer = csv.writer(f)
            writer.writerow((data['NumberOfCores'],
                             data['socket'],
                             data['Form_factor'],
                             data['type_ram'],
                             data['clock_frequency'],
                             data['volume_ram'],
                             data['frequency_ram'],
                             data['volume_video'],
                             data['volume_hdd'],
                             data['PowerSupply'],
                             data['price'],
                             data['type_case']))

def main():

    load_json = [
        'data/case/work_office.json',
        'data/case/home.json',
        'data/case/games.json']


    for json_path in load_json:
        print("load items: %s" % json_path)
        items = SearchItemLoader.load(json_path)

        datas = []

        for item in items:
            NumberOfCores = item.characteristics['NumberOfCores']
            socket = item.characteristics['socket']
            clock_frequency = item.characteristics['clock_frequency']
            Form_factor = item.characteristics['Form_factor']
            volume_ram = item.characteristics['volume_ram']
            type_ram = item.characteristics['type_ram']
            frequency_ram = item.characteristics['frequency_ram']
            volume_video = item.characteristics['volume_video']
            volume_hdd = item.characteristics['volume_hdd']
            PowerSupply = item.characteristics['PowerSupply']
            price = item.price
            type_case = item.type
            NumberOfCores = re.findall(r'\d+', NumberOfCores)
            clock_frequency = re.findall(r'\d+', clock_frequency)
            volume_ram = re.findall(r'\d+', volume_ram)
            frequency_ram = re.findall(r'\d+', frequency_ram)
            volume_video = re.findall(r'\d+', volume_video)
            volume_hdd = re.findall(r'\d+', volume_hdd)
            PowerSupply = re.findall(r'\d+', PowerSupply)

            data = {
                'NumberOfCores': NumberOfCores,
                'socket': socket,
                'Form_factor': Form_factor,
                'type_ram': type_ram,
                'clock_frequency': clock_frequency,
                'volume_ram': volume_ram,
                'frequency_ram': frequency_ram,
                'volume_video': volume_video,
                'volume_hdd': volume_hdd,
                'PowerSupply': PowerSupply,
                'price': price,
                'type_case': type_case
            }
            datas.append(data)
            print("count: %s" % len(datas))
    write_cvs(datas)


if __name__ == '__main__':
    print("Start data case...")
    main()







