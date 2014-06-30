from simpy import *
from Customer import *
from GlobalDeclaration import *
from BankController import *
import random, math
import numpy as np
import scipy as sp

class Arrival(Process):
    """ Source generates cars at random
        Arrivals are at a time-dependent rate
    """
    def __init__(self,env,name):
        self.env = env
        #"name" is the name of the place that we're arriving at.
        #e.g: If we're simulating an arrival in Hotel1, name = "Hotel1"
        self.name = name

    def generate(self,resource):
        i=0
        while (self.env.now < G.maxTime):
            tnow = self.env.now
            print tnow
            arrivalrate =  100 + 10 * math.sin(math.pi * tnow/12.0)
            print arrivalrate
            t = random.expovariate(arrivalrate)
            yield self.env.timeout(t)
            c = Customer(env,"Customer%02d" % (i))
            timeStaying = random.expovariate(1.0/G.staytime)
            env.process(c.visit(resource,timeStaying))
            i += 1

if __name__ == '__main__':
    env = Environment()
    a = Arrival(env,"hotel")
    tb = BankController(env, 2)
    env.process(a.generate(tb.teller))
    env.run(until = G.maxTime)