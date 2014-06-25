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
        self.number_of_QS = number_of_QS
     	self.number_of_KS = number_of_KS
        self.number_of_QD = number_of_QD
        self.number_of_KD = number_of_KD
        """when first build the hotel, no rooms are checked out
        the numbers in the array represent checked QS,KS,QD,KD in sequence"""

     	#self.checked = {'Queen Standard':0,'King Standard':0,'Queen Deluxe':0,'King Deluxe':0]
        self.checked = [0,0,0,0]
        self.room_cost = ROOM_COST[level]
        self.room_price = ROOM_PRICE[level]
        self.revenue = 0

    #need to be fixed later
    #return the string representation of the hotel
    def _str_(self):
        return "Your " + self.name + " is a " + self.level + " hotel "

    def BuyHotel(self,player):
        player.BuyProperty(self.initial_cost())



    #the cost for first building a hotel with certain number of rooms
    def initial_cost(self):
        #return the initial cost for buiding the hotel, in thousand representation
     	return self.number_of_QS*self.room_cost['Queen Standard'] + \
     	self.number_of_KS*self.room_cost['King Standard'] + self.number_of_QD*self.room_cost['Queen Deluxe'] +\
        + self.number_of_KD*self.room_cost['King Deluxe'] + BUILDING_COST[self.level]
    

    def checkout_a_room(self,type):
        if type == 'Queen Standard':
             if self.checked[0] < self.number_of_QS: 
         	 	self.checked[0] = self.checked[0] +1
        if type == 'King Standard':
             if self.checked[1] < self.number_of_KS: 
                self.checked[1] = self.checked[1] +1
        if type == 'Queen Deluxe':
             if self.checked[2] < self.number_of_QS: 
                self.checked[2] = self.checked[2] +1
        if type == 'King Deluxe':
             if self.checked[3] < self.number_of_KS: 
                self.checked[3] = self.checked[3] +1
        print "here"
        self.revenue = self.revenue + self.room_price[type]




if __name__ == '__main__':
    
    #testing
    h = Hotel('Jinjing Garden' ,'Express Inn',6,6,5,5)
    
    



   










