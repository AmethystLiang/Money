#
#  ystockquote : Python module - retrieve stock quote data from Yahoo Finance
#
#  Copyright (c) 2007,2008,2013 Corey Goldberg (cgoldberg@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  Requires: Python 2.7/3.3+

try:
    # py3
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # py2
    from urllib2 import Request, urlopen
    from urllib import urlencode

import simpy

class Stock:

    def __init__(self, symbol):
        self.symbol = symbol
        self.transaction_history = {}
        self.amount = 0
        self.price = 0
        
    def get_historical_prices(self,start_date,end_date):
        
        """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYY-MM-DD'

    Returns a nested dictionary (dict of dicts).
    outer dict keys are dates ('YYYY-MM-DD')"""
 
    
        params = urlencode({
        's': self.symbol,
        'a': int(start_date[5:7]) - 1,
        'b': int(start_date[8:10]),
        'c': int(start_date[0:4]),
        'd': int(end_date[5:7]) - 1,
        'e': int(end_date[8:10]),
        'f': int(end_date[0:4]),
        'g': 'd',
        'ignore': '.csv',
        })
        
        url = 'http://ichart.yahoo.com/table.csv?%s' % params
        days = urlopen(url).readlines()
        data = [day[:-2].split(',') for day in days]
        price = (float(data[1][1]) + float(data[1][2]))/2
        return price

    def buy_record(self,price,amount):
        p  = Transaction(price,amount,True) #buy
        self.transaction_history.append(p) #add this purchase record to the transaction history


    def sell_record(self,price,amount):
        p = Transaction(price,amount,False) #sell
        self.transaction_history.append(p) #add this sell record to the transaction history

    def calculate_money_paid(self):
        money = 0 
        for history in self.purchase_history:
            money += history.price * history.amount



class Transaction:
    def __init__(self,price,amount,is_buy):
        self.price = price
        self.amount = amount
        self.is_buy = is_buy 



if __name__ == '__main__':
    stock = Stock('GE')
    print stock.get_historical_prices('2003-08-19','2003-08-19')

