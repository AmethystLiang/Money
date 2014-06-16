#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simulated world where Neil runs a series of business.
The simulation include a virtue clock, the clock counts days instead of seconds"""

from simpy import *
from GameFunction import *


#still need to do a vitue digital clock


#create an environment for the virture world 
env = Environment()
week = 0
month = 1
year = 2014


def clock(env,tick):
	while True: 
		#print the current week
		week = env.now
		#print "%s %d" %('week',week)

		#process continue until one week after
		yield env.timeout(tick)





#run the world 
if __name__ == '__main__':
	print "Welcome to Neil's World! " + '\n'+  "Make your own fortune to buy Jinjing a BMW ~ " + '\n'+ message1
	enter(message1)


	env.process(clock(env,1))
	#run for 10000 week
	env.run(until = 100)

