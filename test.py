import urllib
import datetime
from Stock import *
# Note that the rstrip strips the trailing newlines and carriage returns before
# printing the output.



if __name__ == '__main__':
 	STOCKS = {'GE':0,'MSFT':0,'WMT':0,'TM':0,'BAC':0,'JPM':0,'INTC':0,'CSCO':0}
 	del STOCKS['GE']
 	print STOCKS.copy()