message1 = "press enter to play"

#Check whether the key press is "ENTER",if yes, continue
def EnterOrExit(message):
	x = raw_input()
	if x == "":
		#need to add link to next level. Now just an empty action
		return 
	#if the keypress is not "ENTER", print the prompt again
	if x == "q":
		return


