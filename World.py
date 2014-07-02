#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simulated world where Neil runs a series of business.
The simulation include a virtual clock, the clock counts days instead of seconds"""

from simpy import *
from GlobalDeclaration import *
import Hotel 
import HotelController as HC
import Player
import GameFunction as gf 

class World():
	"""So, what it would do first is setup the environment: Create a player, create the other controllers, and start the time keeping (simulation of time)
	Now, within it, it'd call the other controllers."""
	def __init__(self, env):
		self.env = env

	env = Environment()
	#starting time
	week = 0
	month = 1
	year = 2014
	#ToDo: a virtual digital clock

	#start running the game.
	def run(self, hc, player):
		while True:
			hc.build_new_hotel(player)
			hc.run(player)
			#below here runs every '10' units. So make the thing that runs every week to go here
			yield self.env.timeout(10)
			hc.build_new_hotel(player)

	#test part, not really in use
	def clock(self, tick):
		while True: 
			#print the current week
			self.week = self.env.now
			print "%s %d" %('week',self.week)
			#process continue until one week after
			yield self.env.timeout(tick)

	def GameCycle(cycletime):
		yield self.env.timeout(cycletime)


#run the world 
if __name__ == '__main__':
	#greetings 
	print "Welcome to Neil's World! " + '\n'+  "Make your own fortune to buy Jinjing a BMW ~ " 
	#Option to enter the game or not 
	gf.EnterGame()
	#Todo: Ask for player's name
	env = Environment()
	world = World(env)
	p = Player.Player('Neil')
	hc = HC.HotelController(world.env)
	world.env.process(world.run(hc, p))
	world.env.run(until = G.maxTime)