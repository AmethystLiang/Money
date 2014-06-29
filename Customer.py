""" bank01_OO: The single non-random Customer """
from simpy import *  #1
## Model components -----------------------------
class Customer(Process):   
    def __init__(self,name):
        self.name =  name  


    def visit(self, timeInBank):
        print("%2.1f %s  Here I am" % (self.sim.now(), self.name))
        yield evn.timeout(timeInBank)
        print("%2.1f %s  I must leave" %(self.sim.now(), self.name))


if __name__ == '__main__':
    env = Environment()
    Neil = Customer(name = "Neil")
    print Neil.name
    env.process(Neil.visit(5))
    env.run(until=50)