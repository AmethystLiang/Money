""" bank01_OO: The single non-random Customer """
from simpy import *  #1
## Model components -----------------------------
class Customer(Process):   
    def __init__(self,env,name):
        self.env = env
        self.name =  name  


    ##need to add in the time in the place part
    def visit(self,resource,stay_duration):
        """wait in line and get the resource.
        For reference,see http://simpy.readthedocs.org/en/latest/simpy_intro/shared_resources.html"""
        with resource.request() as req:
            yield req

            print "%s arrives at %d" %(self.name,self.env.now)
            yield self.env.timeout(stay_duration)
            print "%s leaves at %d" %(self.name,self.env.now)
##need to add in the request part


