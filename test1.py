import math
from simpy import *


#test
if __name__ == '__main__':
	env = Environment()
	env.run(until = 50)
	print "Week %d has passed." %((env.now/7)+1)
	