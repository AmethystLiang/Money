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
        print self.STOCKS.keys()
        print "Enter the ticker name to buy the stock your want "
        stock_name = Tools.get_option("Enter the name below",self.STOCKS.keys())
        print "You chose %s 's stock" %stock_name
        current_date = Tools.current_date(self.start_date,self.env)
        stock = self.STOCKS[stock_name]
        stock_price = float(stock.get_historical_prices(current_date,current_date))
        #return   #for test
        print "The current price of the stock is %f dolars per share. " %stock_price
        wanna_buy = Tools.check_confirm("Enter Y to continue buy this stock. Enter N to exit")
        if wanna_buy:
            print "Please enter the number of shares you want to buy."
            amount =Tools.check_positive_valid_input("Enter your number below:")
            cost = amount*stock_price
            print "The cost for buying %d shares of %s stock is %f dollars" %(amount,stock_name,cost)
            print "The commision fee is 30 dollars." #also deduct the commision fee
            if self.player.buy_property(cost+30,"Sorry, you don't have enough money for buying the stock."):
                stock.purchase_record(stock_price,amount)  #record that the stock with the price.
        else :
            return
    
    #simulate how easy you 
    def price_match():
        pass


    def sellStock(self):
        #make a copy of the list of stocks available 
        purchased_stock = self.update_purchase()
        #if no stock has been purchased
        if not purchased_stock) :
            print "You don't have any stock to sell. Please buy a stock first."
            return
        stock_name = Tools.get_option("Enter the ticker name to sell your chosen stock.",purchased_stock.keys())
        current_date = Tools.current_date(self.start_date,self.env)
        stock = self.STOCKS[stock_name]
        stock_price = float(stock.get_historical_prices(current_date,current_date))
        #return   #for test
        print "The current price of the stock is %f dolars per share. " %stock_price
        for history in stock.purchase_history:
            print "%d shares of this stock was purchase with price %d per share." %(history.amount,history.price)
        wanna_sell = Tools.check_confirm("Enter Y to continue sell this stock. Enter N to exit")
        if wanna_sell:
            max_amount = stock.amount
            print "Please enter the number of shares you want to sell. The maximum number of share you can sell is %d" %stock.amount
            amount =Tools.check_positive_valid_input("Enter your number below:")
            gain = amount*stock_price
            print "The money you gained from selling %d shares of %s stock is %f dollars" %(amount,stock_name,gain)
            print "The net gain from this stock is %d dollars " %(gain - stock.calculate_money_paid())
            stock.amount -= amount # record how many shares you have purchased
            self.player.add_money(gain)  #save the money to player's account
            if amount == stock.amount :
                stock.purchased = 0   #record that all shares of the stock are sold           
        else :
            return

    def update_purchase(self):
        purchased_stock = self.STOCKS.copy()
        for ticker in purchased_stock.keys():
            #the purchase history for that stock is empty
            if not self.STOCKS[ticker].transaction_history  : 
                del purchased_stock[ticker]  #removed the not purchased stock from the list 
            else : 
                pass
        return purchased_stock

if __name__ == '__main__':
    player = Player('Neil')
    env = Environment()
    sc = StockController(player,env)
    sc.setup()
    #sc.buyStock()
    env.run()
    










