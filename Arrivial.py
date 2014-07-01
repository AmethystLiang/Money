from simpy import *
from Customer import *
from GlobalDeclaration import *  #import global parameters from class G
from BankController import *
import random, math

class Arrival():
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
            #generate a semi-random arrivalrate
            arrivalrate =  100 + 10 * math.sin(math.pi * tnow/12.0)
            t = random.expovariate(arrivalrate)
            yield self.env.timeout(t)
            #after a random time, generate a new customer
            c = Customer(env,"Customer%02d" % (i))
            #the customer stays for a random long time period
            timeStaying = random.expovariate(1.0/G.staytime)
            #call the customer "visit()"method that takes in two arguements
            env.process(c.visit(resource,timeStaying))
            i += 1

if __name__ == '__main__':
    env = Environment()
    a = Arrival(env,"hotel")
    tb = BankController(env, 2)
    #for the bank, the resouce is the tb.teller
    env.process(a.generate(tb.teller))
    env.run(until = G.maxTime)