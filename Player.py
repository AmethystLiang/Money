"""a instance of a player for the game."""
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


	def BuyPropety(self, cost):
		if self.money < cost:
			print "You do not have enough money to purchase this." + '\n' + "You are " + cost-self.money + "dollars short"
		else:
			subtractMoney(cost)
			print "Propety purchased"


#test Player 
if __name__ == '__main__':
	p = Player('Jinjing')
	p.subtractMoney(5000)
	print p.money


