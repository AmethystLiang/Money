"""an instance of a player for the game."""
class Player:
	#constructor :
	def __init__(self,name):
		self.name = name 
		self.money = 500000


	def get_money(self):
		return self.money


	def add_money(self,amount):
		self.money += amount


	def subtract_money(self,amount):
		self.money -= amount


	"""return True if the player has enough money to buy the property and deduct money from the player.Return
	false if the player doesn't have enough money"""
	def buy_property(self, cost):
		if self.money < cost:
			print "You do not have enough money to purchase this. Please make another choice."
			return False 
		else:
			self.subtract_money(cost)
			print "Propety purchased"
			return True 
			


#test Player 
if __name__ == '__main__':
	p = Player('Jinjing')
	print p.buy_property(100)