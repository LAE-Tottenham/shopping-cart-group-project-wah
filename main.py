from currency_exchange_tool import currency_convert
from shop_functions import start_shop

currencies={
    'GBP':1,
    'USD':0.77,
    'CAD':0.56,
    'BDT':0.0064,
    'CNY':0.11}
def forex():
    
print('Welcome to my shop')

while True:
    print('Please select what you would like to buy')
    items_to_buy = start_shop()

    # blah blah 
