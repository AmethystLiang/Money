from simpy import *
from Customer import *

class BankController():
    """This bank simulates a bank. Customers can go into the bank and carry out transactions"""
    def __init__(self, env, num_tellers):
        self.env = env
        self.teller = Resource(env, num_tellers)

if __name__ == '__main__':
    env = Environment()
    tb = BankController(env, 1)
    Neil = Customer(env,"Neil")
    Jinjing = Customer(env,"Jinjing")
    env.process(Neil.visit(tb.teller,5))
    env.process(Jinjing.visit(tb.teller,5))
    env.run(until=50)

    