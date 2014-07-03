from Hotel import *
from Player import *
from Tools import *
from simpy import *
from Customer import *
from Arrival import *
from GlobalDeclaration import *  #import global parameters from class G
import random, math
import Menu


#messages to be chosed to put before asking user to give an input
m1 = 'Enter your choice :'
m2 = 'Enter your number :'
"""It prompts the user to make an int input. If the input is not an int, it will ask the user to enter again """

"""an instance of a controller for hotel.
"""
class HotelController:
    #create an array of hotel objects
    def __init__(self,env):
        self.hotels = []
        self.env = env

    #helper funcition for "build_new_hotel(self,player)"
    def buy_hotel(self,hotel,player):
        a = player.buy_property(hotel.initial_cost())
        return a 


    def build_new_hotel(self,player):
        print "press 1 for Express Inn .The cost is 100000" + '\n' + "press 2 for Holiday Inn." 
        print "press 3 for Three Star Hotel" + '\n' + "press 4 for Four Star Hotel"
        print "press 5 for Five Star Hotel " 
        #make sure user are pressing the right key 
        #get pressed key from user
        x = check_positive_valid_input(m1) 
        while x > 5:
            print "Not a valid input. Please enter a valid input"
            x = check_valid_input(m1)
        #use dictionary to choose hotel from input
        print x
        type = ('Express Inn',
                'Holiday Inn',
                'Three Star',
                'Four Star',
                'Five Star'
                )[x-1]
        print "You choose to build a %s Hotel" %type 
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
        #actually buy the hotel object created
        if self.buy_hotel(hotel,player):
            #add the newly built hotel to the array
            self.hotels.append(hotel)
            print "Conguationlations for having your first %s hotel : %s. The total cost of building the hotel is %s" %(hotel.level,hotel.name,hotel.initial_cost())
        else:
            return


    def generate(self):
        i=0
        while (self.env.now < G.maxTime):
            tnow = self.env.now
            #generate a semi-random arrivalrate
            arrivalrate =  100 + 10 * math.sin(math.pi * tnow/12.0)
            t = random.expovariate(arrivalrate)
            #check whether we need to stop while waiting to create another customer
            #Added a check before every yeild report to make sure the weeklyreport doesn't happen during the yield
            if (self.env.now + t) %7 < t :
                yield self.env.timeout(t-(self.env.now + t) %7)
                print self.env.now
                yield self.env.process(Menu.WeeklyReport(self.env,self))
                yield self.env.timeout((self.env.now + t) %7)
            else :
                yield self.env.timeout(t)
           
            #after a random time, generate a new customer
            c = Customer(self.env,"Customer%02d" % (i))
            #the customer stays for a random long time period
            timeStaying = random.expovariate(1.0/G.staytime)
            #call the customer "visit()"method that takes in two arguements
            self.env.process(c.visit_hotel(timeStaying, self))
            """need to fix the problem that once the simulation stopped before the timeStaying finishes,
            how could we make sure we're calculating using the right time?.Namely, the transition part between
            weeks."""
            i += 1


    def customer_flow(self,hotel):
        #need to add generator of customers for more types of rooms
        self.env.process(self.generate())
    

    #don't actually need this,since the resouce part already took care of it    
    def checkout_a_room(hotel,type):
        if hotel.checked[type] < hotel.dic_total_rooms[type] : 
            hotel.checked[type] += 1
        print "here"
        hotel.revenue = hotel.revenue + hotel.room_price[type]
        
    #run the simulation
    def run(self,player):
        #create a new hotel
        self.build_new_hotel(player)
        self.update()
        
    #get revenue from the simulation
    def update(self):
        #iterate through the list of hotel we have, and create customer_flow for them
        for hotel in self.hotels:
            self.customer_flow(hotel)

if __name__ == '__main__':
    env = Environment()
    p = Player('Neil')
    hc = HotelController(env)
    a = Hotel(env,"Jinjing",'Three Star',5,6,5,6)
    print hc.buy_hotel(a,p)