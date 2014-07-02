import math, random
from Hotel import *
""" bank01_OO: The single non-random Customer """
from simpy import *  
import Menu
from HotelController import *
from GlobalDeclaration import *


class Customer():   
    def __init__(self,env,name):
        self.env = env
        self.name =  name  


    #for hotel customer, the stay_duration is how many days they'll stay in a hotel room.
    #Also need to add in the type of room that they're checking in, etc. Namely, more complicated features that works in Hotel Model 
    def visit(self,resource,stay_duration,hotel,roomtype,hc):
        """wait in line and get the resource.
        For reference,see http://simpy.readthedocs.org/en/latest/simpy_intro/shared_resources.html"""
        
        #may need to change here to reflect that customers leave once they can't find a room
        with resource.request() as req:
            yield req


            print "%s arrives at %d" %(self.name,self.env.now)
            #Added a check before every yeild report to make sure the weeklyreport doesn't happen during the yield
            if (self.env.now + math.ceil(stay_duration) ) %7 < math.ceil(stay_duration) :
                yield self.env.timeout(math.ceil(stay_duration)-(self.env.now + math.ceil(stay_duration)) %7)
                yield self.env.process(Menu.WeeklyReport(self.env,hc))
                yield self.env.timeout((self.env.now + math.ceil(stay_duration)) %7)
            else :
                yield self.env.timeout(math.ceil(stay_duration))
            print "%s leaves at %d" %(self.name,self.env.now)
            hotel.revenue += hotel.room_price[roomtype]*math.ceil(stay_duration) #math.ceil(),get the upper rounded number

    #for hotel customer, the stay_duration is how many days they'll stay in a hotel room.
    #Also need to add in the type of room that they're checking in, etc. Namely, more complicated features that works in Hotel Model 
    def visit_hotel(self,resource,stay_duration,hotel):
        """wait in line and get the resource.
        For reference,see http://simpy.readthedocs.org/en/latest/simpy_intro/shared_resources.html"""
        
        #random hotel room type number
        """random_type_number = random.randint(0,len(Hotel.ROOM_TYPES)-1)
        room_type = Hotel.ROOM_TYPES[random_type_number]
        #check if the room is full -- if it is, try a different type
        initial_random = random_type_number
        while (hotel.simpy_rooms[room_type].capacity - hotel.simpy_rooms[room_type].count) != 0:
            random_type_number = (random_type_number + 1) % len(Hotel.ROOM_TYPES)
            room_type = Hotel.ROOM_TYPES[random_type_number]
            if initial_random == random_type_number:
                #TODO: If the entire hotel is full, try a different hotel
                break"""

        print 
        #may need to change here to reflect that customers leave once they can't find a room
        with resource.request() as req:
            yield req
            print "%s arrives at %d" %(self.name,self.env.now)
            yield self.env.timeout(math.ceil(stay_duration))
            print "%s leaves at %d" %(self.name,self.env.now)
            hotel.revenue += hotel.room_price[room_type]*math.ceil(stay_duration) #math.ceil(),get the upper rounded number
            print hotel.revenue



