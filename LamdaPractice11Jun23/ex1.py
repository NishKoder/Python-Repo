# lambda sorted
products = [{
    'name': 'nishant',
    'value': 30000
},
{
    'name': 'nishantg',
    'value': 40000
},{
    'name': 'gnishant',
    'value': 20000
},{
    'name': 'ggnishant',
    'value': 35000
}]

sorted_products = sorted(products, key = lambda x: x['value'])

for product in sorted_products:
    print(product)