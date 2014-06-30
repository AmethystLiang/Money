from Hotel import *
from Player import *
from Tools import *


#messages to be chosed to put before asking user to give an input
m1 = 'Enter your choice :'
m2 = 'Enter your number :'
"""It prompts the user to make an int input. If the input is not an int, it will ask the user to enter again """

"""an instance of a controller for hotel.
"""
class HotelController:
	#create an array of hotel objects
	def __init__(self):
		self.hotels = []

	def buy_hotel(self,hotel,player):
		player.buy_property(hotel.initial_cost())


	def new_hotel(self,player):
		print "press 1 for Express IThis simulates a hotel. Customers can go into the hotel and check in a roomnn. The cost is 100000" + '\n' + "press 2 for Holiday Inn." 
		print "press 3 for Three Star Hotel" + '\n' + "press 4 for Four Star Hotel"
		print "press 5 for Five Star Hotel " 
		#make sure user are pressing the right key 
		#get pressed key from user
		x = check_positive_valid_input(m1) 
		while x > 4:
			print "Not a valid input. Please enter a valid input"
			x = check_valid_input(m1)
		#use dictionary to choose hotel from input
		print x
		type = ('Express Inn',
				'Holiday Inn',
				'Three Star',
				'Four Star',
				'Five Star'
				)[x]
		print "You choose to build a %s Hotel" %type 
		#name your hotel
		print "Please Name your hotel"
		name = raw_input()
		#should put in the range of hotels that you can choose to build later
		#put in number of different types of rooms
		print "How many Queen Standard rooms would you like to have ? "
		QS = check_positive_valid_input(m2)
		print "How many Queen Deluxe rooms would you like to have ? "
		QD = check_positive_valid_input(m2)
		print "How many King Standard rooms would you like to have ? "
		KS = check_positive_valid_input(m2)
		print "How many King Deluxe rooms would you like to have ? "
		KD = check_positive_valid_input(m2)
		#build a hotel object
		hotel = Hotel(name,type,QS,QD,KS,KD)
		#actually buy the hotel object created
		if self.buy_hotel(hotel,player):
			#add the newly built hotel to the array
			self.hotels.append(hotel)
			print "Conguationlations for having your first %s hotel : %s. The total cost of buildign the hotel is %s" %(hotel.level,hotel.name,hotel.initial_cost())
		else:
			return

	def checkout_a_room(hotel,type):
		if hotel.checked[type] < hotel.dic_total_rooms[type] : hotel.checked[type] += 1
		print "here"
		hotel.revenue = hotel.revenue + hotel.room_price[type]
		

	def run(self,player):
		self.new_hotel(player)


	def update(self):
		pass

if __name__ == '__main__':
	c = Player('Neil')
	a = HotelController()
	b = Hotel('Jinjing Garden' ,'Express Inn',6,6,5,5)
	print a.buy_hotel(b,c)

