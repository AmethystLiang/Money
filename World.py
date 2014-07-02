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
import Menu


"""So, what it would do first is setup the environment: Create a player, create the other controllers, and start the time keeping (simulation of time)
Now, within it, it'd call the other controllers."""



#still need to do a virtue digital clock

#start running the game.
def run(player,hc,env):
    hc.run(player)
    

        

#starting time
week = 0
month = 1
year = 2014






#run the world 
if __name__ == '__main__':
    #greetings 
    print "Welcome to Neil's World! " + '\n'+  "Make your own fortune to buy Jinjing a BMW ~ " 
    #Option to enter the game or not 
    Menu.EnterGame()
    p = Player.Player('Neil')
    #An event that may happen at some point in time.
    env = Environment()
    #create a hotel controller
    hc = HC.HotelController(env)
    run(p,hc,env)
    env.run(until = 20)