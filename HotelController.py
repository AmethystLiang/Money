from Hotel import *
from Player import *


#messages to be chosed to put before asking user to give an input
m1 = 'Enter your choice :'
m2 = 'Enter your number :'
"""It prompts the user to make an int input. If the input is not an int, it will ask the user to enter again """
def checkValidInput(m):
	is_valid = 0 
	choice = 0
	while not is_valid:
		try: 
			choice = int(raw_input(m))
			is_valid = 1
		except ValueError,e :
			print "Not a valid input. Please press the right key"
			checkValidInput(m)
		return choice

"""an instance of a controller for hotel"""
class HotelController:
	#create an array of hotel objects
	def __init__(self):
		self.hotels = []

	def BuyHotel(self,hotel,player):
		player.BuyProperty(hotel.initial_cost())


	def NewHotel(self,player):
		print "press 1 for Express Inn. The cost is 100000" + '\n' + "press 2 for Holiday Inn." 
		print "press 3 for Three Star Hotel" + '\n' + "press 4 for Four Star Hotel"
		print "press 5 for Five Star Hotel " 
		#make sure user are pressing the right key 
		#get pressed key from user
		x = checkValidInput(m1) 
		while x > 5 :
			print "Not a valid input. Please press the right key"
			x = checkValidInput(m1)
		#use dictionary to choose hotel from input
		type = {
			1 : 'Express Inn',
			2 : 'Holiday Inn',
			3 : 'Three Star',
			4 : 'Four Star',
			5 : 'Five Star'
			}.get(x)  
		print "You choose to build a %s Hotel" %type 
		#name your hotel
		print "Please Name your hotel"
		name = raw_input()
		#should put in the range of hotels that you can choose to build later
		#put in number of different types of rooms
		print "How many Queen Standard rooms would you like to have ? "
		QS = checkValidInput(m2)
		print "How many Queen Deluxe rooms would you like to have ? "
		QD = checkValidInput(m2)
		print "How many King Standard rooms would you like to have ? "
		KS = checkValidInput(m2)
		print "How many King Deluxe rooms would you like to have ? "
		KD = checkValidInput(m2)
		#build a hotel object
		hotel = Hotel(name,type,QS,QD,KS,KD)
		#actually buy the hotel object created
		if self.BuyHotel(hotel,player):
			#add the newly built hotel to the array
			self.hotels.append(hotel)
			print "Conguationlations for having your first %s hotel : %s. The total cost of buildign the hotel is %s" %(hotel.level,hotel.name,hotel.initial_cost())
		else:
			return
		

	def run(self,player):
		self.NewHotel(player)


	def update(self):
		pass

if __name__ == '__main__':
	c = Player('Neil')
	a = HotelController()
	b = Hotel('Jinjing Garden' ,'Express Inn',6,6,5,5)
	print a.BuyHotel(b,c)

