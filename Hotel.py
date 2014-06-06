#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import module support
#import support

#facility cost for different levels of hotels
#will replace these with more realistic data later
BUILDING_COST = [100,150,200,250,300]
SINLGE_ROOM_COST = [2,3,4,5]
DOUBLE_ROOM_COST=[3,4,5,6]

#Hotel
""" Every hotel you built is an instance of the hotel class.when you first build a hotel,
    you can decide the initial level of your hotel (e.g : 4-star) The level set the basic cost
    for the basic facilities of your hotel.It also influence on the cost of each room. """

class Hotel:
    def __init__(self,number_of_singles,number_of_doubles,level):
     	self._number_of_singles = number_of_singles
     	self._number_of_doubles = number_of_doubles
     	self._level = level
     	self._checked_singles = number_of_singles
     	self._checked_doubles = number_of_doubles
    
    

    def get_number_of_singles(self):
     	return self._number_of_singles;
    
    #getter for field number_of_doubles
    def get_number_of_doubles(self):
     	return self._number_of_doubles;
    
    #@getter
    def get_checked_singles(self):
     	return self._checked_singles;

    def get_checked_doubles(self):
        return self._checked_doubles;
    
    #@setter
    def set_number_of_singles(self,number):
     	self._number_of_singles = number
     
    #@setter
    def set_number_of_doubles(self,number):
     	self._number_of_doubles = number
    
    def raw_cost(self):
     	return self._number_of_singles*SINLGE_ROOM_COST[self.level] + \
     	self._number_of_doubles*DOUBLE_ROOM_COST[self.level] + BUILDING_COST[self.level];
    
    def check_a_room(self,number):
        if number == 1:
     	 	self._checked_singles = self._checked_singles +1
        else:
            self._checked_doubles = self._checked_doubles +1






if __name__ == '__main__':
    
    #testing
    h = Hotel(5,6,2)
    h.check_a_room(1)
    print h. get_number_of_singles()

   










