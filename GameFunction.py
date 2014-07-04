import sys
import World as wd
from Hotel import *
#Check whether the key press is "ENTER",if yes, continue
def EnterGame():
	print "Press enter to play." + '\n' + "Press q to exit the game"
	x = raw_input()
	if x == "":
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



	

