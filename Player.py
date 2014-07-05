from GlobalDeclaration  import *
import os

"""an instance of a player for the game."""
class Player:
	#constructor :
	def __init__(self,name):
		self.name = name 
		self.money = G.player_initial_money


	def get_money(self):
		return self.money


	def add_money(self,amount):
		self.money += amount


	def subtract_money(self,amount):
		self.money -= amount


	"""return True if the player has enough money to buy the property and deduct money from the player.Return
	false if the player doesn't have enough money"""
	def buy_property(self, cost,m):
		if self.money < cost:
			os.system("clear")
			print m
			return False 
		else:
			self.subtract_money(cost)
			print "Propety purchased"
			print "You now have %d dollars" %self.money
			return True 
			


#test Player 
if __name__ == '__main__':
	p = Player('Jinjing')
	print p.buy_property(100)