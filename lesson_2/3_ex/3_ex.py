import yaml

data = {
    'items': ['iPhone SE', 'iPhone 7', 'iPhone 8', 'iPhone Xs'],
    'items_quantity': 4,
    'items_price': {
        'iPhone SE': '500$',
        'iPhone 7': '600$',
        'iPhone 8': '700$',
        'iPhone Xs': '900$'
                    }
        }

with open('yaml_test.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

with open('yaml_test.yaml', 'r', encoding='utf-8') as f:
    data_check = yaml.load(f,Loader=yaml.SafeLoader)

print(data == data_check)