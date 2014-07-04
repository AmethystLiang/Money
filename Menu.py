import sys
import os
import math
import World as wd
from Hotel import *
import Tools
from GlobalDeclaration import *
#Check whether the key press is "ENTER",if yes, continue
def EnterGame():
	print "Press Enter to paly.Press q to exit the game"
	x = raw_input()
	if x == "":
		#need to add link to next level. Now just an empty action
		os.system("clear")
		return
	#if press q, then exit the whole program
	if x == "q":
		sys.exit()
	#if the keypress is not "ENTER", print the prompt again
	else: 
		print "please press the right key "
		EnterGame()
	

def WeeklyReport(env,hc):
	while G.reported != round(env.now/7) :
		G.reported = round(env.now/7) 
		yield env.timeout(0)
		yield env.process(Tools.weekly_report_notice(env))
		
		print "Week %d has passed." %math.ceil(G.reported)  #announce the current week
		#hand control back to simpy
		for hotel in hc.hotels:
			hotel.str()   #announce the money made, hotel room numbers 

		print "Would you want to updrade any of your hotel ?"  #ask whether the user wanna upgrade the hotel
		if Tools.check_confirm("Print Y for yes. Print N to continue playing"):
			os.system("clear") #clear screen
			choice = int(Tools.get_option("""You have several upgrade options:
Enter 1 to build more rooms in your original hotel. The upper limit for each type of rooms is 50.
Enter 2 to upgrade your hotel to a higher level. 
Enter 3 to build a new hotel """,[1,2,3]))
			if choice == 1 :
				Upgrade_Hotel(hc)
			if choice == 2:
				pass	
			if choice == 3:
				pass	

		else:
			os.system("clear") #clear the screen
		print "Done weekly report. Starting week %d " %(G.reported+1)


def Upgrade_Hotel(hc):
	os.system("clear") 
	print "Enter the corresponding number for the hotel you want to build more rooms"
	i = 1
	for hotel in hc.hotels:
		print "Enter %d for %s" %(i,hotel.name)
	hotel = hc.hotels[int(Tools.get_option('Your choice: ',Tools.produce_hotel_option(hc)))-1]
	os.system("clear") 
	print "you choose to upgrade %s " %hotel.name 
	print "%s now have %d Queen Standard rooms,%d King Standard rooms, \
	%d Queen Deluxe rooms and %d King Deluxe rooms" %(hotel.name,hotel.simpy_rooms['Queen Standard'].capacity,\
	hotel.simpy_rooms['King Standard'].capacity,hotel.simpy_rooms['Queen Deluxe'].capacity,\
	hotel.simpy_rooms['King Deluxe'].capacity)

	roomtype = hotel.ROOM_TYPES[int(Tools.get_option("""Which type of rooms would you like to build more? 
	Enter 1 for Queen Standard,
	Enter 2 for King Standard,
	Enter 3 for Queen Deluxe,
	Enter 4 for King Deluxe """,[1,2,3,4]))-1]
	roomnumber = Tools.check_positive_valid_input("How many more rooms would you want to build ? Can only buy %d more" %(50-hotel.simpy_rooms[roomtype].capacity))
	





		








		

	

