"""an instance of a player for the game."""
class Player:
	#constructor :
	def __init__(self,name):
		self.name = name 
		self.money = 500000


	def getMoney(self):
		return self.money


	def addMoney(self,amount):
		self.money += amount


	def subtractMoney(self,amount):
		self.money -=amount


	"""return True if the player has enough money to buy the property and deduct money from the player.Return
	false if the player doesn't have enough money"""
	def BuyProperty(self, cost):
		if self.money < cost:
			print "in if"
			print "You do not have enough money to purchase this." 
			return False 
		else:
			self.subtractMoney(cost)
			print "Propety purchased"
			return True


#test Player 
if __name__ == '__main__':
	p = Player('Jinjing')
	p.subtractMoney(5000)
	print p.money


