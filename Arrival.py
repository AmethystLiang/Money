from simpy import *
from Customer import *
from GlobalDeclaration import *  #import global parameters from class G
from BankController import *
import random, math

class Arrival():
    """ Source generates customers at random
        Arrivals are at a time-dependent rate
    """
    def __init__(self,env):
        self.env = env
        #"name" is the name of the place that we're arriving at.
        #e.g: If we're simulating an arrival in Hotel1, name = "Hotel1"
        #not using this now

    

if __name__ == '__main__':
    #test
   """ env = Environment()
    a = Arrival(env,"hotel")
    tb = BankController(env, 2)
    #for the bank, the resouce is the tb.teller
    env.process(a.generate(tb.teller))
    env.run(until = G.maxTime)"""