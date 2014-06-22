#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simulated world where Neil runs a series of business.
The simulation include a virtue clock, the clock counts days instead of seconds"""

from simpy import *
import GameFunction as gf
import Hotel 

#initial money you have
money = 500000 

#still need to do a virtue digital clock


#create an environment for the virture world 
env = Environment()
#starting time
week = 0
month = 1
year = 2014


def clock(env,tick):
	while True: 
		#print the current week
		week = env.now
		print "%s %d" %('week',week)

		#process continue until one week after
		yield env.timeout(tick)



#run the world 
if __name__ == '__main__':
	#greetings 
	print "Welcome to Neil's World! " + '\n'+  "Make your own fortune to buy Jinjing a BMW ~ " 
	#Option to enter the game or not 
	gf.EnterGame()
	gf.BuyLand()
	gf.BuildHotel()
	env.process(clock(env,1))
	#test : run for 5 week
	env.run(until = 5)

