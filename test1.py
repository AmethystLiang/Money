import math
from simpy import *
from Tools import *
from Menu import *



#enviroment test 
"""env = Environment()
	env.run(until = 50)
	print "Week %d has passed." %((env.now/7)+1)"""

#test
if __name__ == '__main__':
	get_option("""You have several options:
Enter 1 to build more rooms in your original hotel. The upper limit for each type of rooms is 50.
Enter 2 to upgrade your hotel to a higher level. 
Enter 3 to build a new hotel """)
	

	
	