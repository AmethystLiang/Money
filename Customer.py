""" bank01_OO: The single non-random Customer """
from simpy import *  #1
## Model components -----------------------------
class Customer():   
    def __init__(self,name):
        self.name =  name  


    def visit(self, timeInBank):
        print("%2.1f %s  Here I am" % (self.sim.now(), self.name))
        yield evn.timeout(timeInBank)
        print("%2.1f %s  I must leave" %(self.sim.now(), self.name))


if __name__ == '__main__':
    env = Environment()
    neil = Customer(name = "Neil")
    print neil.name
    
    #Do the following inside the bnak controller instea dof the customer. 
    #Infact, it may be possible to delete this class entirely and instead just used the player as the customer. 
    #That'd make sense UNLESS you are going to the level of generating random customers visiting a bank and you as a player must
    # wait in line for the next avalialble teller. Let's dicuss this later --Neil

    #env.process(Neil.visit(5))
    #env.run(until=50)