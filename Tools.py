#input check reference: http://learnpythonthehardway.org/book/ex48.html


def check_valid_input(m):
	try: 
		return int(raw_input(m))
	except ValueError,e :
		print "Not a valid input. Please enter a valid input"
		return check_valid_input(m)


def check_positive_valid_input(m):
	choice = -1
	try: 
		choice = (int(raw_input(m)))
		if choice < 0 : raise ValueError()
	except ValueError,e :
		print "Not a valid input. Please enter a valid input"
		return check_valid_input(m)
	return choice

def EnterGame(m):
	print m
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
		EnterGame(m)