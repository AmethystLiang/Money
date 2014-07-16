from Stock import *
import random 
import datetime
import Tools
from Player import *
from simpy import *


class StockController:

    """
    Constructor
    """
    def __init__(self,player,env):
        self.player =  player
        self.env = env
        #could later use a SQL to store more available stocks
        self.STOCKS = {'GE':0,'MSFT':0,'WMT':0,'TM':0,'BAC':0,'JPM':0,'INTC':0,'CSCO':0,'KO':0,'PEP':0,'VZ':0,'GOOG':0,'TWX':0,'DELL':0,'MS':0,'AAPL':0}
        #randomly generate a start date
        self.start_date = datetime.date(random.randrange(2001,2006), 01, 01)


    def setup(self):
        #create an array of stock objects based on the Tickers array 
        #self.STOCKS.keys() represent the ticker names of the stocks
        for ticker in self.STOCKS.keys():
            self.STOCKS[ticker] = Stock(ticker)



    def buyStock(self):
        #could have a input box for user to enter 
        print "The stocks you can buy are :"
        for ticker in self.STOCKS.keys():
            if self.STOCKS[ticker].purchased == 0 :
                print ticker 
        print "Enter the ticker name to buy the stock your want "
        stock_name = Tools.get_option("Enter the name below",self.STOCKS.keys())
        print "You chose %s 's stock" %stock_name
        date_collapsed = datetime.timedelta(days=self.env.now*7) #calculate how many days have passed since the start date
        current_date = str(self.start_date + date_collapsed)  # calculate the date of which the stock price we wanna get
        stock = self.STOCKS[stock_name]
        print current_date
        stock_price = float(stock.get_historical_prices(current_date,current_date))
        #return   #for test
        print "The current price of the stock is %f dolars per share. " %stock_price
        wanna_buy = Tools.check_confirm("Enter Y to continue buy this stock. Enter N to exit")
        if wanna_buy:
            print "Please enter the number of shares you want to buy."
            amount =Tools.check_positive_valid_input("Enter your number below:")
            cost = amount*stock_price
            print "The cost for buying %d shares of %s stock is %f dollars" %(amount,stock_name,cost)
            if self.player.buy_property(cost,"Sorry, you don't have enough money for buying the stock."):
                self.STOCKS[stock_name].purchased = 1   #record that the stock is purchased
                self.STOCKS[stock_name].amount = amount # record how many shares you have purchased
        else :
            return
         
    def sellStock(self):
        #Todo: implment the self stock option
        pass


if __name__ == '__main__':
    player = Player('Neil')
    env = Environment()
    sc = StockController(player,env)
    sc.setup()
    #sc.buyStock()
    env.run(until = 200)
    










