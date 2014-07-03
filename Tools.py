#input check reference: http://learnpythonthehardway.org/book/ex48.html
from simpy import *
from HotelController import *


#check valid int input
def check_valid_input(m):
    try: 
        print m
        return int(raw_input())
    except ValueError,e :
        print "Not a valid input. Please enter a valid input"
        return check_valid_input(m)


def check_positive_valid_input(m):
    choice = -1
    try: 
        print m
        choice = int(raw_input())
        if choice < 0 : raise ValueError()
    except ValueError,e :
        print "Not a valid input. Please enter a valid input"
        return check_valid_input(m)
    return choice

#check whether the input in y or n
def check_confirm(m):
    print m 
    x =raw_input()
    if x == "y":
        result = True
        return result
    if x == "n":
        result = False
        return result 
    else : 
        print "Not a valid input. Please enter a valid input"
        check_confirm(m)


#return the input number
def get_option(m):
    result = check_positive_valid_input(m)
    #result is not 1 or 2
    if result >3 : 
        print "Not a valid input. Please enter a valid input"
        result = get_option(m)
    return result


def hotel_upgrade_option():
    option = get_option("""You have several options:
Enter 1 to build more rooms in your original hotel. The upper limit for each type of rooms is 50.
Enter 2 to upgrade your hotel to a higher level. 
Enter 3 to build a new hotel """)
    if option == 1:
        #ToDo: build the actual funtionality for option 1.
        #for now, just print
        print "in option 1" 
    if option == 2:
        #ToDo: build the actual funtionality for option 2.
        #for now, just print 
        print "in option 2"
    if option == 3: 
        #build a new hotel
        print "in option 3"






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