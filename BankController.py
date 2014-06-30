from simpy import *
from Customer import *

class BankController():
    """This bank simulates a bank. Customers can go into the bank and carry out transactions"""
    def __init__(self, env, num_tellers):
        self.env = env
        self.teller = Resource(env, num_tellers)

    def visit(self, customer):
        yield self.env.timeout(5)
        print "You are visiting a bank"


if __name__ == '__main__':
    env = Environment()
    tb = Bank(env, 2)
    neil = Customer(name = "Neil")
    print neil.name + " hi"
    env.process(tb.visit(neil))
    env.run(until=50)