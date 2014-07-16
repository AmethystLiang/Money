import sys
import os
import math
import World as wd
from Hotel import *
import Tools
from GlobalDeclaration import *
from StockController import *
from BankController import *

class Menu:

    def __init__(self,player,env,hc,sc,bc):
        self.player = player
        self.env = env
        self.hc = hc
        self.sc = sc
        self.bc = bc

#Check whether the key press is "ENTER",if yes, continue
    def EnterGame(self):
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




    def WeeklyReport(self):
        while G.reported != round(self.env.now/7) :
            G.reported = round(self.env.now/7) 
            yield self.env.timeout(0)
            yield self.env.process(Tools.weekly_report_notice(self.env))
            print "Week %d has passed." %math.ceil(G.reported)  #announce the current week
            #hand control back to simpy
            self.revenue_report()
            if G.tillPay == 0 :
                self.bc.pay_loan() #has to pay loan before doing other stuff
            while True:
                choice = int(Tools.get_option("Enter 1 for hotel upgrade. Enter 2 to check out bank. Enter 3 to check out stock.Enter 4 to skip and continue.",[1,2,3,4]))
                os.system("clear") #clear screen
                if choice == 1:
                    yield self.env.process(self.hotel_upgrade())
                if choice == 2:
                    #ToDo : add in the bank part 
                    yield self.env.process(self.bank_business())
                if choice == 3:
                    self.sc.buyStock()
                if choice == 4 :
                    break
            G.tillPay -= 1   #loan payment countdown
            print "Done weekly report." +'\n' + "Starting week %d " %(G.reported+1)
            Tools.Continue()
    

    def revenue_report(self):
        for hotel in self.hc.hotels:
                hotel.str()   #announce the money made, hotel room numbers 
                self.player.add_money(hotel.revenue)
        print "You now have %d dollars. " % self.player.checking_account.balance


    def hotel_upgrade(self):
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
                    yield self.env.process(self.build_hotel_rooms())
                if choice == 2:
                    yield self.env.process(self.upgrade_hotel())
                if choice == 3:
                    yield self.env.process(self.new_hotel()) 

    def build_hotel_rooms(self):
        os.system("clear") 
        print "Enter the corresponding number for the hotel you want to build more rooms"
        i = 1
        for hotel in self.hc.hotels:
            print "Enter %d for %s" %(i,hotel.name)
        hotel = self.hc.hotels[int(Tools.get_option('Your choice: ',Tools.produce_hotel_option(self.hc)))-1]
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
            you can only build %d rooms of this type" %(self.player.checking_account.balance/hotel.room_cost[roomtype])
        roomnumber = hotel.simpy_rooms[roomtype].capacity + 1
        upgrade_cost = checking_account.balance + 1
        while True :
            while roomnumber > (hotel.simpy_rooms[roomtype].capacity - hotel.init_room_number[roomtype]):
                message = "How many more rooms would you want to build ? Can only buy %d more" %(hotel.simpy_rooms[roomtype].capacity - hotel.init_room_number[roomtype])
                roomnumber = Tools.check_positive_valid_input(message)
            upgrade_cost = hotel.room_cost[roomtype]*roomnumber
            if self.player.buy_property(upgrade_cost,m):
                break   
        #change the record of room number for that type of room 
        hotel.init_room_number[roomtype] += roomnumber 
        yield hotel.simpy_rooms[roomtype].put(roomnumber)  #actually build the roomssimpy_rooms[roomtype].put[roomnumber]   #actually build the rooms
        print "Successfully built %d more %s rooms for your %s" %(roomnumber,roomtype,hotel.name)


    def upgrade_hotel(self):
        os.system("clear") 
        print "Enter the corresponding number for the hotel you want to upgrade"
        i = 1
        for hotel in self.hc.hotels:
            print "Enter %d for %s" %(i,hotel.name)
            i += 1
        hotel = self.hc.hotels[int(Tools.get_option('Your choice: ',Tools.produce_hotel_option(self.hc)))-1]
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
        cost_after_upgrade = Hotel(self.env,'test',upgrade_options[option],hotel.simpy_rooms['Queen Standard'].capacity,\
            hotel.simpy_rooms['King Standard'].capacity,hotel.simpy_rooms['Queen Deluxe'].capacity,\
            hotel.simpy_rooms['King Deluxe'].capacity).initial_cost()

        if self.player.buy_property(cost_after_upgrade - hotel.initial_cost(),"You don't have enough money to upgrade your hotel "):
            hotel.level = upgrade_options[option]
            print "Successfully upgrade your hotel to %s" %hotel.level
        yield self.env.timeout(0)  


    def new_hotel(self):
        os.system("clear")
        self.hc.build_new_hotel(self.player) 
        yield self.env.timeout(0)  



    def bank_business(self):
        os.system("clear")
        print "Welcome to Jinjing's Bank!"
        while True :
            choice1 = int(Tools.get_option("""Enter 1 to tranfer money from cheking account to saving account.
        Enter 2 to transfer money from saving account to checking account.
        Enter 3 to loan money from bank.
        Enter 4 to exit.""",[1,2,3,4]))
            if choice1 == 1:
                self.bc.checking_to_saving()
            if choice1 == 2:
                self.bc.saving_to_checking()
            if choice1 == 3 :
                self.bc.loan()
            if choice1 == 4 :
                break



