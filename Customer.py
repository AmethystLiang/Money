""" bank01_OO: The single non-random Customer """
from simpy import *  
class Customer():   
    def __init__(self,env,name):
        self.env = env
        self.name =  name  


    #for hotel customer, the stay_duration is how many days they'll stay in a hotel room.
    #Also need to add in the type of room that they're checking in, etc. Namely, more complicated features that works in Hotel Model 
    def visit(self,resource,stay_duration):
        """wait in line and get the resource.
        For reference,see http://simpy.readthedocs.org/en/latest/simpy_intro/shared_resources.html"""
        
        #may need to change here to reflect that customers leave once they can't find a room
        with resource.request() as req:
            yield req

            print "%s arrives at %d" %(self.name,self.env.now)
            yield self.env.timeout(stay_duration)
            print "%s leaves at %d" %(self.name,self.env.now)



