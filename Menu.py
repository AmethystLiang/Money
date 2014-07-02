import sys
import math
import World as wd
from Hotel import *
import Tools
from GlobalDeclaration import *
#Check whether the key press is "ENTER",if yes, continue
def EnterGame():
	print "press Enter to paly.press q to exit the game"
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

def WeeklyReport(env,hc):
	while G.reported != round(env.now/7) :
		G.reported = round(env.now/7) 
		print "Week %d has passed." %((env.now/7)+1)  #announce the current week
		#have to do a yield, otherwise can't use this as a process to intterupt other process
		yield env.timeout(0.01)
		for hotel in hc.hotels:
			print "The money you made from %s so far is %d. " %(hotel.name,hotel.revenue) #announce the money made
		print "Done weekly report "
		break

		

	

