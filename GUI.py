#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simulated world where Neil runs a series of business.
The simulation include a virtue clock, the clock counts days instead of seconds"""

from simpy import *
from GlobalDeclaration import *
from PySide import QtCore, QtGui
import Hotel 
import HotelController as HC
import Player
import GameFunction as gf 
import mainWindow
from  Menu import *
from StockController import *
from BankController import *

"""So, what it would do first is setup the environment: Create a player, create the other controllers, and start the time keeping (simulation of time)
Now, within it, it'd call the other controllers."""








class GUI(QtCore.QObject):


    def run(self):
        sim_thread = SimThread()
        #self.connect( self.workThread, QtCore.SIGNAL("update(QString)"), self.add )
        sim_thread.start()
        time.sleep(0.3)

    def thread_test():
        print "testing 1 2 3" 

    def emit_test(self):
        print "testing"
        self.emit(QtCore.SIGNAL('update()'))

    #Setup GUI->python functionailty here
    def setupGUI(self, ui):
        QtCore.QObject.connect(ui.startButton, QtCore.SIGNAL("clicked()"), self.run )
        #ToDo: fix this
        #self.trigger.emit()
        
        QtCore.QObject.connect(ui.buildHotelButton, QtCore.SIGNAL("clicked()"), self.emit_test )
        #QtCore.QObject.connect(ui.buildHotelButton, QtCore.SIGNAL("clicked()"), self.emit(QtCore.SIGNAL('update(QString)')) )

        #Have this emit a signal that connects to a connecter within the sim thread that runs TestThread

my_GUI = GUI()

class SimThread(QtCore.QThread):
 def __init__(self): 
  QtCore.QThread.__init__(self)

 def __del__(self):
  self.wait()
 
 def run(self):
    #still need to do a virtual digital clock
    #Option to enter the game or not 
    p = Player('Neil')
    #An event that may happen at some point in time.
    env = Environment()
    #create a hotel controller
    bc = BankController(env,p)
    hc = HC.HotelController(env,p)
    sc = StockController(p,env)
    menu = Menu(p,env,hc,sc,bc)
    #Todo: Fix this
    QtCore.QObject.connect(my_GUI, QtCore.SIGNAL('update()'), self.add_hotel)
    menu.EnterGame()
    bc.setup()
    sc.setup()
    hc.run(menu)
    env.run()

 def add_hotel(self):
    print "test add hotel"


#run the world 
if __name__ == '__main__':
    #InitialSetup#
    import sys
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #Link Functionailty Here#
    my_GUI.setupGUI(ui)
    #Code to launch the GUI#
    MainWindow.show()
    sys.exit(app.exec_())