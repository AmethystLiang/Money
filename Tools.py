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

#need to be fixed
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
    choice = get_option(m,['y','n'])
    if choice == 'y':
        return True
    else :
        return False

#will added in later
def weekly_report_notice(env):
    yield env.timeout(0)
    print "Weekly Report Time"
   
    EnterGame("Press enter to continue")
    os.system("clear") 
    

#return the option corresponding to the user input. Parameter 
def get_option(m,options):
    print m
    choice = raw_input()
    for option in options:
        if choice == str(option):
            return choice
    print "Not a valid input. Please enter a valid input"
    choice = get_option(m,options)
    return choice



def produce_hotel_option(hc):
    range = []
    i = 0
    while i < len(hc.hotels):
        range.append(i+1)
        i += 1
    return range


def EnterGame(m):
    print m
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
        EnterGame(m)



   