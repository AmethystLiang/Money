#!/usr/bin/python
# -*- coding: utf-8 -*-
from Player import *
from simpy import *

"""facility cost for different types of hotels
    will replace with more realistic data later"""
BUILDING_COST =  {  'Express Inn' : 100000,
    'Holiday Inn' : 150000,
    'Three Star': 200000,
    'Four Star' : 250000,
    'Five Star':350000,
    }
#cost for building different types of hotel rooms
ROOM_COST = { 'Express Inn':{'Queen Standard':800, 'King Standard':900, 'Queen Deluxe':1200, 'King Deluxe':1500 },
    'Holiday Inn':{'Queen Standard':1000, 'King Standard':1200, 'Queen Deluxe':1500, 'King Deluxe':1800},
    'Three Star': {'Queen Standard':1200, 'King Standard':1500, 'Queen Deluxe':1800, 'King Deluxe':2000},
    'Four Star': {'Queen Standard':1500, 'King Standard':2000, 'Queen Deluxe':2500, 'King Deluxe':3000},
    'Five Star': {'Queen Standard':2500, 'King Standard':2800, 'Queen Deluxe':3000, 'King Deluxe':3500}}
#price for different hotel rooms
ROOM_PRICE = { 'Express Inn':{'Queen Standard':80, 'King Standard':100, 'Queen Deluxe':120, 'King Deluxe':150 },
    'Holiday Inn':{'Queen Standard':100, 'King Standard':120, 'Queen Deluxe':150, 'King Deluxe':180},
    'Three Star': {'Queen Standard':120, 'King Standard':150, 'Queen Deluxe':180, 'King Deluxe':200},
    'Four Star': {'Queen Standard':150, 'King Standard':200, 'Queen Deluxe':250, 'King Deluxe':300},
    'Five Star': {'Queen Standard':250, 'King Standard':280, 'Queen Deluxe':300, 'King Deluxe':350}}

"""This simulates a hotel. Customers can go into the hotel and check in a room"""
""" Every hotel you built is an instance of the hotel class.when you first build a hotel,
    you can decide the initial level of your hotel (e.g : 4-star) The level set the basic cost
    for the basic facilities of your hotel.It also influence on the cost of each room. """
class Hotel:
    #Different Types of hotel rooms
    ROOM_TYPES = ['Queen Standard', 'King Standard', 'Queen Deluxe', 'King Deluxe']
    HOTEL_TYPES = ['Express Inn', 'Holiday Inn', 'Three Star','Four Star','Five Star']

    #constructor
    def __init__(self,env,name,level,number_of_QS,number_of_KS,number_of_QD,number_of_KD):
        self.env = env
        self.name = name
        self.level = level
        """when first build the hotel, no rooms are checked out
            the numbers in the array represent checked QS,KS,QD,KD in sequence"""
    
        #self.checked = [0,0,0,0]
        self.room_cost = ROOM_COST[level]
        self.room_price = ROOM_PRICE[level]
        self.revenue = 0
        self.init_room_number = { 
            'Queen Standard': number_of_QS,
            'King Standard': number_of_KS,
            'Queen Deluxe': number_of_QD,
            'King Deluxe': number_of_KD}
        self.simpy_rooms = {
            'Queen Standard':Container(env, init=number_of_QS,capacity = 50),
            'King Standard':Container(env, init=number_of_KS,capacity = 50),
            'Queen Deluxe': Container(env, init=number_of_QD,capacity = 50),
            'King Deluxe': Container(env, init=number_of_KD,capacity = 50)
            }
    
    #need to be fixed later
    #return the string representation of the hotel
    def str(self):
        print "Your %s is a %s hotel ." %(self.name,self.level)
        for roomtype in self.ROOM_TYPES:
            print "%d out of its %d %s are checked out now" \
            %(self.simpy_rooms.get(roomtype).level,self.init_room_number[roomtype],roomtype)
        print "The money you made from %s so far is %d. " %(self.name,self.revenue) 

    
    #the cost for first building a hotel with certain number of rooms
    def initial_cost(self):
        #return the initial cost for buiding the hotel, in thousand representation
        return self.init_room_number['Queen Standard']*self.init_room_number['Queen Standard'] + \
        self.init_room_number['King Standard']*self.init_room_number['King Standard'] + self.init_room_number['Queen Deluxe']*self.room_cost['Queen Deluxe'] +\
        + self.init_room_number['King Deluxe']*self.room_cost['King Deluxe'] + BUILDING_COST[self.level]


if __name__ == '__main__':
    env = Environment()
    #testing
    h = Hotel(env,'Jinjing Garden' ,'Express Inn',6,6,5,5)
    h.str()