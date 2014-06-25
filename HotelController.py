from Hotel import *

"""an instance of a controller for hotel"""
class HotelController:
	#create an array of hotel objects
	def __init__(self):
		self.hotels = []


	def NewHotel(self,player):
		print "press 1 for Express Inn. The cost is 100000" + '\n' + "press 2 for Holiday Inn" 
		print "press 3 for Three Star Hotel" + '\n' + "press 4 for Four Star Hotel"
		print "press 5 for Five Star Hotel " 
		print "press N for cancel"
		#make sure user are pressing the right key 
		#get pressed key from user
		x = input()
		if isinstance(x,int) and x<6: 
		#use dictionary to choose hotel from input
			type = {
				1 : 'Express Inn',
				2 : 'Holiday Inn',
				3 : 'Three Star',
				4 : 'Four Star',
				5 : 'Five Star'
				}.get(x)  
			print "You choose to build a %s" %type 
			#name your hotel
			print "Please Name your hotel"
			name = raw_input()
			#should put in a range of hotels 
			#put in number of different types of rooms
			print "How many Queen Standard rooms would you like to have ? "
			QS = raw_input()
			print "How many Queen Deluxe rooms would you like to have ? "
			QD = input()
			print "How many King Standard rooms would you like to have ? "
			KS = input()
			print "How many King Deluxe rooms would you like to have ? "
			KD = input()
			#build a hotel object
			hotel = Hotel(name,type,QS,QD,KS,KD)
			#actually buy the hotel object created
			if hotel.BuyHotel(player):
				#add the newly built hotel to the array
				self.hotels.append(hotel)
				print "Conguationlations for having your first %s hotel : %s. The total cost of buildign the hotel is %s" %(hotel.level,hotel.name,hotel.initial_cost())
			else:
				return
		else:
			print "please press the right key"
			self.NewHotel(player)

	def run(self,player):
		self.NewHotel(player)


	def update(self):
		pass



