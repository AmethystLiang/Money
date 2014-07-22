#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simulated world where Neil runs a series of business.
The simulation include a virtue clock, the clock counts days instead of seconds"""

from simpy import *
from GlobalDeclaration import *
import Hotel 
import HotelController as HC
import Player
import GameFunction as gf 
from  Menu import *
from StockController import *
from BankController import *

"""So, what it would do first is setup the environment: Create a player, create the other controllers, and start the time keeping (simulation of time)
Now, within it, it'd call the other controllers."""



#still need to do a virtue digital clock

#start running the game.
def run(hc,sc,menu):
    bc.setup()
    sc.setup()
    hc.run(menu)
    







#run the world 
if __name__ == '__main__':
    #Option to enter the game or not 
    p = Player('Neil')
    #An event that may happen at some point in time.
    env = Environment()
    #create a hotel controller
    bc = BankController(env,p)
    hc = HC.HotelController(env,p)
    sc = StockController(p,env)
    menu = Menu(p,env,hc,sc,bc)
    os.system("clear")
    menu.EnterGame()
    run(hc,sc,menu)
    env.run()

