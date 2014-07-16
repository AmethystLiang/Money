import os
from Hotel import *
from Player import *
from Tools import *
from simpy import *
from Customer import *
from GlobalDeclaration import *  #import global parameters from class G
import random, math
from Menu import *


#messages to be chosed to put before asking user to give an input
m1 = 'Enter your choice :'
m2 = 'Enter your number :'
"""It prompts the user to make an int input. If the input is not an int, it will ask the user to enter again """

"""an instance of a controller for hotel.
"""
class HotelController:
    #create an array of hotel objects
    def __init__(self,env,player):
        self.hotels = []
        self.env = env
        self.player = player

    #helper funcition for "build_new_hotel(self,player)"
    def buy_hotel(self,hotel):
        a = self.player.buy_property(hotel.initial_cost(),"You do not have enough money to purchase this. Please make another choice.")
        return a 


    def build_new_hotel(self):
        print "The money you have now is %d" %self.player.checking_account.balance
        print "Press 1 for Express Inn .The cost is 100000" + '\n' + "Press 2 for Holiday Inn. The cost is 150000" 
        print "Press 3 for Three Star Hotel.The cost is 200000" + '\n' + "Press 4 for Four Star Hotel.The cost is 250000"
        print "Press 5 for Five Star Hotel.The cost is 350000 " 
        #make sure user are pressing the right key 
        #get pressed key from user
        x = check_positive_valid_input(m1) 
        while x > 5:
            print "Not a valid input. Please enter a valid input"
            x = check_valid_input(m1)
        #use dictionary to choose hotel from input
        type = ('Express Inn',
                'Holiday Inn',
                'Three Star',
                'Four Star',
                'Five Star'
                )[x-1]
        os.system("clear") #clear screen
        print "You choose to build a %s Hotel" %type 
        print "It will cost %d for the building. " %BUILDING_COST[type]
        print "The money you'll have if build this building is %d dollars" %(self.player.checking_account.balance-BUILDING_COST[type])
        if BUILDING_COST[type]>self.player.checking_account.balance: 
            os.system("clear")
            if type == 'Express Inn':
                print "You can't afforf to build any hotel now"
                return
            print "You can't afford to build hotel of this type"
            self.build_new_hotel()
            return
        #name your hotel
        print "Please Name your hotel"
        name = raw_input()
        #should put in the range of hotels that you can choose to build later
        #put in number of different types of rooms
        print "How many Queen Standard rooms would you like to have ? "
        QS = check_positive_valid_input(m2)
        print "How many Queen Deluxe rooms would you like to have ? "
        QD = check_positive_valid_input(m2)
        print "How many King Standard rooms would you like to have ? "
        KS = check_positive_valid_input(m2)
        print "How many King Deluxe rooms would you like to have ? "
        KD = check_positive_valid_input(m2)
        #build a hotel object
        hotel = Hotel(self.env,name,type,QS,QD,KS,KD)
        print hotel.initial_cost()
        #actually buy the hotel object created
        os.system("clear")
        if self.buy_hotel(hotel):
            #add the newly built hotel to the array
            self.hotels.append(hotel)
            print "Conguationlations for having your %s hotel : %s. The total cost of building the hotel is %s" %(hotel.level,hotel.name,hotel.initial_cost())
        else:
            self.build_new_hotel()
           


    def generate_flow(self,menu):
        i=0
        while (self.env.now < G.maxTime):
            time_now = self.env.now
            #generate a semi-random arrivalrate
            arrival_rate =  10 + 1 * math.sin(math.pi * time_now/12.0)
            #produce a random number that follows an expotential distribution with parameter arrivalrate*2
            t = random.expovariate(arrival_rate*2)
            #check whether we need to stop while waiting to create another customer
            #Added a check before every yeild report to make sure the weeklyreport doesn't happen during the yield
            if (self.env.now + t) %7 < t :
                yield self.env.timeout(t-(self.env.now + t) %7)
                yield self.env.process(menu.WeeklyReport())
                yield self.env.timeout((self.env.now + t) %7)
            else :
                yield self.env.timeout(t)
            #after a random time, generate a new customer
            c = Customer(self.env,"Customer%02d" % (i))
            #the customer stays for a random long time period
            time_staying = random.expovariate(1.0/G.staytime)
            #call the customer "visit()"method that takes in two arguements
            self.env.process(c.visit_hotel(time_staying,self,self.player,menu))
            i += 1


    #run the simulation
    def run(self,menu):
        #create a new hotel
        self.build_new_hotel()
        Continue()
        self.update(menu)

        
    #get revenue from the simulation
    def update(self,menu):
        self.env.process(self.generate_flow(menu))

if __name__ == '__main__':
    env = Environment()
    p = Player('Neil')
    hc = HotelController(env)
    a = Hotel(env,"Jinjing",'Three Star',5,6,5,6)
    print hc.buy_hotel(a,p)