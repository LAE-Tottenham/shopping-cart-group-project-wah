import math # you'll probably need this

exchange_rates = {
    'USD': 1.13, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.15,
    'CNY': 9.23,
    'BDT': 155.30,
    'ZAR': 22.90
}

def check_currency_exists(currency_rate):
    if currency_rate in exchange_rates.keys():
        return currency_rate

def currency_convert(original_c, new_c, amount):
    if amount<10 or amount>1000:
        return ('amount must be between £10 and £1000')
    if not check_currency_exists(original_c):
        return ('original currency not supported')
    if not check_currency_exists(new_c):
        return('new currency not supported')
    new_amount=amount*exchange_rates[new_c]
    return round(new_amount,2)
    
    
