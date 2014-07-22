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


import simpy



        

try:
    # py3
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # py2
    from urllib2 import Request, urlopen
    from urllib import urlencode

import simpy
from GlobalDeclaration import *

class Stock:

    def __init__(self, symbol):
        self.symbol = symbol
        self.transaction_history = []
        self.amount = 0
        self.money_paid = 0
        self.money_gained = 0

        
    def get_historical_prices(self,start_date,end_date):
        
        """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYY-MM-DD'

    Returns a nested dictionary (dict of dicts).
    outer dict keys are dates ('YYYYMMDD')
 
        url = 'http://ichart.yahoo.com/table.csv?s=%s&' % self.symbol + \
              'd=%s&' % str(int(end_date[5:7]) - 1) + \
              'e=%s&' % str(int(end_date[8:10])) + \
              'f=%s&' % str(int(end_date[0:4])) + \
              'g=d&' + \
              'a=%s&' % str(int(start_date[5:7]) - 1) + \
              'b=%s&' % str(int(start_date[8:10])) + \
              'c=%s&' % str(int(start_date[0:4])) + \
              'ignore=.csv'"""
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
        # http://ichart.yahoo.com/table.csv?s=<string>&a=<int>&b=<int>&c=<int>&d=<int>&e=<int>&f=<int>&g=d&ignore=.csv
        # http://ichart.yahoo.com/table.csv?a=0&ignore=.csv&s=GE&b=1&e=1&d=0&g=d&f=2004&c=2004
        url = 'http://ichart.yahoo.com/table.csv?%s' % params
        days = urlopen(url).readlines()
        data = [day[:-2].split(',') for day in days]
        price = (float(data[1][1]) + float(data[1][2]))/2
        return price

    def buy_record(self,price,amount):
        p  = Transaction(self.symbol,price,amount,True,G.reported) #buy
        self.transaction_history.append(p) #add this purchase record to the transaction history


    def sell_record(self,price,amount):
        p = Transaction(self.symbol,price,amount,False,G.reported) #sell
        self.transaction_history.append(p) #add this sell record to the transaction history

    def calculate_money(self,cost,is_buy):
            if is_buy == True:
                self.money_paid += cost
            else :
                self.money_gained += cost


    def check_transaction(self):
        if not self.transaction_history:
            print "You don't have any transaction history for this stock."
            return
        for transaction in self.transaction_history :
            transaction.check_transaction()



class Transaction:
    def __init__(self,symbol,price,amount,is_buy,week):
        self.symbol = symbol
        self.price = price
        self.amount = amount
        self.is_buy = is_buy
        self.week = week

    def check_transaction(self):
        if self.is_buy :
            buy = 'bought'
        else :
            buy = "sold"
        print "Week %d , you %s %d shares of %s stock for %d dollars per share." %(self.week,buy,self.amount,self.symbol,self.price)

if __name__ == '__main__':
    stock = Stock('GE')
    print stock.get_historical_prices('2003-08-19','2003-08-19')

