import sys
import os
import math
import World as wd
from Hotel import *
import Tools
from GlobalDeclaration import *
#Check whether the key press is "ENTER",if yes, continue
def EnterGame():
    os.system("clear")
    print "Welcome to Neil's World! " + '\n'+  "Make your own fortune to buy Jinjing a BMW ~ " 
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




def WeeklyReport(env,hc,player):
    while G.reported != round(env.now/7) :
        G.reported = round(env.now/7) 
        yield env.timeout(0)
        yield env.process(Tools.weekly_report_notice(env))

        print "Week %d has passed." %math.ceil(G.reported)  #announce the current week
        #hand control back to simpy
        for hotel in hc.hotels:
            hotel.str()   #announce the money made, hotel room numbers 
            player.money += hotel.revenue
        print "You now have %d dollars. " %player.money
        while True: 
            print "Would you want to updrade any of your hotel ?"  #ask whether the user wanna upgrade the hotel
            upgrade = Tools.check_confirm("Print Y for yes. Print N to continue playing")
            if not upgrade:
                os.system("clear") #clear the screen
                break
            os.system("clear") #clear screen
            choice = int(Tools.get_option("""You have several upgrade options:
Enter 1 to build more rooms in your original hotel. The upper limit for each type of rooms is 50.
Enter 2 to upgrade your hotel to a higher level. 
Enter 3 to build a new hotel """,[1,2,3]))
            if choice == 1 :
                yield env.process( build_hotel_rooms(env,hc,player))
            if choice == 2:
                yield env.process(upgrade_hotel(env,hc,player))
            if choice == 3:
                yield env.process(new_hotel(env,hc,player))   
        print "Done weekly report." +'\n' + "Starting week %d " %(G.reported+1)
        Tools.Continue()
        yield env.timeout(0)

def build_hotel_rooms(env,hc,player):
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
    hotel.init_room_number['King Standard'],hotel.init_room_number['Queen Deluxe'],\
    hotel.init_room_number['King Deluxe'])

    roomtype = hotel.ROOM_TYPES[int(Tools.get_option("""Which type of rooms would you like to build more? 
    Enter 1 for Queen Standard,
    Enter 2 for King Standard,
    Enter 3 for Queen Deluxe,
    Enter 4 for King Deluxe """,[1,2,3,4]))-1]
    
    m = "Sorry, you do not have enough money to build this many rooms." + '\n' + "With all your money,\
        you can only build %d rooms of this type" %(player.money/hotel.room_cost[roomtype])
    roomnumber = hotel.simpy_rooms[roomtype].capacity + 1
    upgrade_cost = player.money + 1
    while True :
        while roomnumber > (hotel.simpy_rooms[roomtype].capacity - hotel.init_room_number[roomtype]):
            message = "How many more rooms would you want to build ? Can only buy %d more" %(hotel.simpy_rooms[roomtype].capacity - hotel.init_room_number[roomtype])
            roomnumber = Tools.check_positive_valid_input(message)
        upgrade_cost = hotel.room_cost[roomtype]*roomnumber
        if player.buy_property(upgrade_cost,m):
            break   
    #change the record of room number for that type of room 
    hotel.init_room_number[roomtype] += roomnumber 
    yield hotel.simpy_rooms[roomtype].put(roomnumber)  #actually build the roomssimpy_rooms[roomtype].put[roomnumber]   #actually build the rooms
    print "Successfully built %d more %s rooms for your %s" %(roomnumber,roomtype,hotel.name)


def upgrade_hotel(env,hc,player):
    os.system("clear") 
    print "Enter the corresponding number for the hotel you want to upgrade"
    i = 1
    for hotel in hc.hotels:
        print "Enter %d for %s" %(i,hotel.name)
    hotel = hc.hotels[int(Tools.get_option('Your choice: ',Tools.produce_hotel_option(hc)))-1]
    os.system("clear") 
    print "You choose to upgrade %s. " %hotel.name
    print "Your %s is a %s now" %(hotel.name,hotel.level) 
    upgrade_options = Tools.upgrade_option(hotel)
    i = 0
    choice = []
    while i< len(upgrade_options):
        if upgrade_options[i] is None:
            print "Can't upgrade anymore."
            break
            return
        else :
            print "Press %d to upgrade %s to a %s. " %(i+1,hotel.name,upgrade_options[i])
            choice.append(i+1)
            i += 1
    option = int(Tools.get_option("Enter your choice:",choice))-1
    cost_after_upgrade = Hotel(env,'test',upgrade_options[option],hotel.simpy_rooms['Queen Standard'].capacity,\
        hotel.simpy_rooms['King Standard'].capacity,hotel.simpy_rooms['Queen Deluxe'].capacity,\
        hotel.simpy_rooms['King Deluxe'].capacity).initial_cost()

    if player.buy_property(cost_after_upgrade - hotel.initial_cost(),"You don't have enough money to upgrade your hotel "):
        hotel.level = upgrade_options[option]
        print "Successfully upgrade your hotel to %s" %hotel.level
    yield env.timeout(0)  


def new_hotel(env,hc,player):
    os.system("clear")
    hc.build_new_hotel(player) 
    yield env.timeout(0)  






