import sys
import World as wd
from Hotel import *
#Check whether the key press is "ENTER",if yes, continue
def EnterGame():
	print "press enter to play." + '\n' + "press q to exit the game"
	x = raw_input()
	if x == "":
		#need to add link to next level. Now just an empty action
		return
	#if press q, then exit the whole program
	if x == "q":
		sys.exit()
	#if the keypress is not "ENTER", print the prompt again
	else: 
		print "please press the right key "
		EnterGame()

#This is the second scene. It appears as soon as you enter the game 
def BuyLand():
	print "Hi there. You have 500,000 $ and a land for sale at 100,000 $ at your city to build a hotel." 
	print "Would you like to buy this land? " + '\n' + "Enter Y for yes and enter N to exit." 
	x = raw_input()
	if x == "y":
		wd.money = wd.money - 100000
		print "Conguatulations,now you have your own land to build a hotel! " + \
		'\n' + "your remaining asset is %d dollars" %wd.money
		return
	if x == "n":
		sys.exit()
	else: 
		print "please press the right key :"
		BuyLand()

#once you have a land, you can build a hotel
def BuildHotel():
	#but actually , the charater might not have enough money to build some type of hotel
	print "Now you own a land, which type of hotel do you want to build? "
	print "press 1 for Express Inn. The cost is 100000" + '\n' + "press 2 for Holiday Inn" 
	print "press 3 for Three Star Hotel" + '\n' + "press 4 for Four Star Hotel"
	print "press 5 for Five Star Hotel " 
	#get pressed key from user
	x = input()
	#make sure user are pressing the right key 
	if isinstance(x,int) and x<6: 
		#use dictionary to choose hotel from input
		type = {
	        1 : 'Express Inn',
	        2 : 'Holiday Inn',
	        3 : 'Three Star',
	        4 : 'Four Star',
	        5 : 'Five Star'
	        }.get(x)  

	    # if not enough money to choose this type of hotel
		if BUILDING_COST.get(type) > wd.money:
			print "Not enough money for this type of hotel,please choose a cheaper one. "
		else :
			print "You choose to build a %s" %type 
			print "Please Name your hotel"
			name = raw_input()
			#should put in a range of hotels 
			print "How many Queen Standard rooms would you like to have ? "
			QS = input()
			print "How many Queen Deluxe rooms would you like to have ? "
			QD = input()
			print "How many King Standard rooms would you like to have ? "
			KS = input()
			print "How many King Deluxe rooms would you like to have ? "
			KD = input()
			hotel1 = Hotel(name,type,QS,QD,KS,KD)
			print "Conguationlations for having your first %s hotel : %s. The total cost of buildign the hotel is %s" %(hotel1.level,hotel1.name,hotel1.initial_cost())
	else : 
		print "please press the right key"
		BuildHotel()

	

