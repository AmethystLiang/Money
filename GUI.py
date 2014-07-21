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



#still need to do a virtue digital clock

#start running the game.
def run():
    #Option to enter the game or not 
    p = Player('Neil')
    #An event that may happen at some point in time.
    env = Environment()
    #create a hotel controller
    bc = BankController(env,p)
    hc = HC.HotelController(env,p)
    sc = StockController(p,env)
    menu = Menu(p,env,hc,sc,bc)
    menu.EnterGame()
    bc.setup()
    sc.setup()
    hc.run(menu)
    env.run()


#starting time
week = 0
month = 1
year = 2014


#Setup GUI->python functionailty here
def setupGUI(ui):
    QtCore.QObject.connect(ui.startButton, QtCore.SIGNAL("clicked()"), run)
    QtCore.QObject.connect(ui.buildHotelButton, QtCore.SIGNAL("clicked()"), run)

#run the world 
if __name__ == '__main__':
    #InitialSetup#
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #Link Functionailty Here#
    setupGUI(ui)
    #Code to launch the GUI#
    MainWindow.show()
    sys.exit(app.exec_())