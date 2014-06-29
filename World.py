#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simulated world where Neil runs a series of business.
The simulation include a virtue clock, the clock counts days instead of seconds"""

from simpy import *
import Hotel 
import HotelController as HC
import Player
import GameFunction as gf

"""So, what it would do first is setup the environment: Create a player, create the other controllers, and start the time keeping (simulation of time)
Now, within it, it'd call the other controllers."""
p = Player.Player('Neil')
#An event that may happen at some point in time.
env = Environment()
#create a hotel controller
hc = HC.HotelController()


#still need to do a virtue digital clock

#start running the game.
def run(player):
	hc.run(player)

#starting time
week = 0
month = 1
year = 2014

#test part, not really in use
def clock(env,tick):
	while True: 
		#print the current week
		week = env.now
		print "%s %d" %('week',week)
		#process continue until one week after
		yield env.timeout(tick)


def GameCycle(env,cycletime):
	yield env.timeout(cycletime)



#run the world 
if __name__ == '__main__':
	#greetings 
	print "Welcome to Neil's World! " + '\n'+  "Make your own fortune to buy Jinjing a BMW ~ " 
	#Option to enter the game or not 
	gf.EnterGame()
	run(p)
	#env.process(clock(env,1))
	#test : run for 5 week
	#run the game 
	env.run(until = 5)

