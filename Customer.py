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

    def rand_hotel_room(self, hotel_array):
        #Loop through hotels randomly
        random.shuffle(hotel_array)
        #randomly produce a customer preference for rooms
        rand_type_number = random.randint(0,len(Hotel.ROOM_TYPES)-1)
        init_rand_type_number = rand_type_number
        adder = -1 # by default, choose cheaper one if the prefered type is not available
        if rand_type_number == 0:
            adder = 1  #if is already choosing cheaper one, choose a slightly more expensive one
        for hotel in hotel_array:
            #check if the room is full -- if it is, try a different type
            #after two tries, will just give up and go to another hotel
            for i in xrange(2): #only have two tries
                room_type = Hotel.ROOM_TYPES[rand_type_number]
                if (hotel.simpy_rooms[room_type].capacity - hotel.simpy_rooms[room_type].count) > 0:
                    room_type = Hotel.ROOM_TYPES[rand_type_number]
                    return [hotel, room_type]
                rand_type_number += adder
                #Code to always select the cheapest next available room
            rand_type_number = init_rand_type_number #go back to old preference and choose room in another hotel
        #If there is no hotel/room selected, return nothing
        return None


    #for hotel customer, the stay_duration is how many days they'll stay in a hotel room.
    #Also need to add in the type of room that they're checking in, etc. Namely, more complicated features that works in Hotel Model 
    def visit_hotel(self, stay_duration, hc):
        """wait in line and get the resource.
        For reference,see http://simpy.readthedocs.org/en/latest/simpy_intro/shared_resources.html"""
        #randomly sample and select a hotel
        hotel_room_array = self.rand_hotel_room(hc.hotels)
        if hotel_room_array is None:
            pass #do nothing and give up this customer
        else:
            hotel = hotel_room_array[0]
            roomtype = hotel_room_array[1]
            #may need to change here to reflect that customers leave once they can't find a room
            with hotel.simpy_rooms[roomtype].request() as req:
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