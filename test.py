import math
from simpy import *
from Tools import *
from Menu import *
import os



#enviroment test 
"""env = Environment()
	env.run(until = 50)
	print "Week %d has passed." %((env.now/7)+1)"""

#test
if __name__ == '__main__':
	env = Environment()
	weekly_report_notice(env)

	
	