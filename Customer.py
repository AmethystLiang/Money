#import necessary mathematics and statistics module 
import numpy as num
import scipy as sci
import matplotlib as mat

#import the python simulation package
from simpy import *
 

class Arrival(Sim.Process):
	"""Scource generates costumers at random 


	Arrivals are at a time-dependent rate"""



	def generate(self):
		i = 0
		while (self.sim.now()<G.maxTime):
				tnow = self.sim.now()
				arrivalrate = 100 + 10* math.sin(math.pi *tnow/12.0)
				#the mean arrival rate is a function based on the time during the day
				t = random.expovariate(arrivalrate)
				yield Sim.hold, self,t
				c = Costumers(name = "Costumers%02d"(i),sim=self.sim)
				