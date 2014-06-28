#!/usr/bin/python
# -*- coding: utf-8 -*-
from Player import *



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




""" Every hotel you built is an instance of the hotel class.when you first build a hotel,
    you can decide the initial level of your hotel (e.g : 4-star) The level set the basic cost
    for the basic facilities of your hotel.It also influence on the cost of each room. """
class Hotel:
    #constructor
    #umber_of_singles,number_of_doubles argurments take integers
    #level takes strings
    def __init__(self,name,level,number_of_QS,number_of_KS,number_of_QD,number_of_KD):
        self.name = name
        self.level = level
        #Todo: delete these 4 variables below eventually
        #self.number_of_QS = number_of_QS
        #self.number_of_KS = number_of_KS
        #self.number_of_QD = number_of_QD
        #self.number_of_KD = number_of_KD
        """when first build the hotel, no rooms are checked out
            the numbers in the array represent checked QS,KS,QD,KD in sequence"""
        self.dic_total_rooms = {'Queen Standard':number_of_QS,
            'King Standard':number_of_KS,
            'Queen Deluxe': number_of_QD,
            'King Deluxe': number_of_KD}
        self.dict_checked_out = {'Queen Standard':0,
            'King Standard':0,
            'Queen Deluxe':0,
            'King Deluxe':0}
        #self.checked = [0,0,0,0]
        self.room_cost = ROOM_COST[level]
        self.room_price = ROOM_PRICE[level]
        self.revenue = 0
    
    #need to be fixed later
    #return the string representation of the hotel
    def _str_(self):
        return "Your " + self.name + " is a " + self.level + " hotel "
    
    #the cost for first building a hotel with certain number of rooms
    def initial_cost(self):
        #return the initial cost for buiding the hotel, in thousand representation
        return self.dic_total_rooms['Queen Standard']*self.room_cost['Queen Standard'] + \
        self.dic_total_rooms['King Standard']*self.room_cost['King Standard'] + self.dic_total_rooms['Queen Deluxe']*self.room_cost['Queen Deluxe'] +\
        + self.dic_total_rooms['King Deluxe']*self.room_cost['King Deluxe'] + BUILDING_COST[self.level]


if __name__ == '__main__':
    
    #testing
    h = Hotel('Jinjing Garden' ,'Express Inn',6,6,5,5)