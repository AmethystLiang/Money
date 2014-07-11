from GlobalDeclaration  import *
import os

"""an instance of a player for the game."""
class Player:
	#constructor :
	def __init__(self,name):
		self.name = name 
		self.checking_account = 0
		self.saving_account = 0
		self.credit = G.intial_player_credit
		self.loan = 0 #represent the loan you have to repay


	def set_bank_account(self,checking_account,saving_account):
		self.checking_account = checking_account
		self.saving_account = saving_account
		

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