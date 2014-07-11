#Written for and tested on Python 3.1.
import csv
from urllib import *
def yahoo_quotes_csv_url(tickers):
    return ''.join(('http://finance.yahoo.com/d/quotes.csv?s=',
                    '+'.join(tickers),
                    '&f=snl1'))


    
if __name__ == '__main__':
    tickers = ('GOOG', 'AAPL')
    url = yahoo_quotes_csv_url(tickers)
    print(url)
    urlretrieve(url, 'quotes.csv')
    reader = csv.reader(open('quotes.csv'))
    for row in reader:
        #row[0]=ticker, row[1]=company, float(row[2])=value
        print(row)