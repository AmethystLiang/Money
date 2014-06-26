def check_valid_input(m):
	try: 
		return int(raw_input(m))
	except ValueError,e :
		print "Not a valid input. Please enter a valid input"
		return check_valid_input(m)