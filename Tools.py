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