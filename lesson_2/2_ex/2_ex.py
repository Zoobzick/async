import json


def write_to_json(item, quantity, price, buyer, date):
    data = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    with open("json_output.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4))


write_to_json('Xiaomi Vacuum Robot Cleaner', '1', '229$', 'Troover', '23.04.2023')
