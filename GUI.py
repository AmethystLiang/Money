#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simulated world where Neil runs a series of business.
The simulation include a virtue clock, the clock counts days instead of seconds"""

from simpy import *
from GlobalDeclaration import *
from PySide import QtCore, QtGui
import time
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

class SimThread(QtCore.QThread):
 def __init__(self, GUI): 
  QtCore.QThread.__init__(self)
  self.GUI = GUI

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
    QtCore.QObject.connect(self.GUI, QtCore.SIGNAL('build_hotel()'), self.add_hotel)
    menu.EnterGame()
    bc.setup()
    sc.setup()
    hc.run(menu)
    env.run()

 def add_hotel(self):
    print "test add hotel"


class GUI(QtCore.QObject):
    def run(self):
        sim_thread = SimThread(self)
        sim_thread.start()
        time.sleep(0.3)

    def emit_build(self):
        self.emit(QtCore.SIGNAL('build_hotel()'))

    #Setup GUI->python functionailty here
    def setupGUI(self, ui):
        QtCore.QObject.connect(ui.startButton, QtCore.SIGNAL("clicked()"), self.run )       
        QtCore.QObject.connect(ui.buildHotelButton, QtCore.SIGNAL("clicked()"), self.emit_build )
        

#run the world 
if __name__ == '__main__':
    #InitialSetup#
    import sys
    my_GUI = GUI()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #Link Functionailty Here#
    my_GUI.setupGUI(ui)
    #Code to launch the GUI#
    MainWindow.show()
    sys.exit(app.exec_())