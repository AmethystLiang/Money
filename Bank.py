#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division  # to allow fraction division
from simpy import *
import Player
from GlobalDeclaration import *
from Hotel import *

#when built, the bank has unlimited amount of money
class Bank:
    def __init__(self,player):
        self.money = G.bankMoney
        self.player = player
        self.interest = 0

    #parameter time has unit in month, and interest is counpounded by-weekly 
    #Loan interest rate also taken the player's credit into account. They higher the player credit,the lower the interest rate
    # see http://en.wikipedia.org/wiki/Compound_interest
    #t has to be at least a month
    def interest_rate(self,t,loan_or_not):
        P = 1000 # principle amount 
        S = 0 # value after time t 
        m = 2 # number of times the interest rate is compounded per month
        
        #calculating interest for a loan
        if loan_or_not:
            S = P * (1+G.loan_interest_rate/m)**(G.loan_interest_rate*t)
            return (S - P)/P*(G.intial_player_credit/self.player.credit)*12 #calculate the compounded interest rate taking player credit into account
        
        #calculating interest for a saving account: 
        else : 
            S = P * (1+G. save_interest_rate/m)**(G.save_interest_rate*t)
            return (S - P)/P*12   
            








#super class of different kinds of bank account 
class Account:
    def __init__(self,initial_balance,env):
        self.balance = initial_balance
        #id is a 7 digit number


    def save(self,amount):
        self.balance = self.balance + amount


    def withdraw(self,amount):
        if balance >= amount :
            self.balance = self.balance - amount


    #to be implemented
    def report(self):
        pass
    

#add in the accout features so that characters can manage their money like in real life
class SavingAccount(Account):
    def __init__(self,initial_balance,env):
        Account.__init__(self,initial_balance,env)
        print " A saving account has been created for you"
        self.count = 3
        self.interest = 0


    """The formula for calculating compound interest on a single deposit is: A = P(1 + r/n)^(nt).
Principal (P), the rate of interest (r), the number of years (t), and the number of times the interest is compounded (n). 
The interest earned (A) represents the solution to the equation, and the value of (n) should be 365 for interest compounded daily, 
12 for monthly and 4 for quarterly.

will implement more complicated interest rate feature, now will only use simple models 

return the interest if you save your money for a certain period of time (the unit for time is month)"""

#should also make sure that if it's only saved for 3 month, it's free to withdraw after 3 months.
    def addInterest(self,time):
        #the basci framework refelecting the different interest rate in different saving time period
        #will add in interest for longer time, e.g : 3 yrs, 5 yrs
        #if only save for less than 3 months, the interest rate is 1 % 
        if time <= 3:
            self.balance = self.balance*(1+0.01*time)
        #half a year interest rate
        if time > 3 & time <= 6:
            self.balance = self.balance*(1+0.05*time)
        if time >6 & time <= 12:
            self.balance = self.balance*(1+0.1*time)

    """saving account has a withdraw limit of 3 per month"""
    def withdraw(self,amount):
        #need to find a way to reset count every month
        if self.count <= 3:
            self.balane = self.balance - amount
        else:
            print "out of withdraw chances"
            #will implement a way to continue withdraw with some transaction fee





#simulate an ATM for a checking account
class CheckingAccount(Account):
    def __init__(self,initial_balance,env):
        Account.__init__(self,initial_balance,env)
        print " A checking account has been created for you"



if __name__ == '__main__':
    #test
    env = Environment()
    player = Player('Neil')
    checking_account = CheckingAccount(G.player_initial_money,env) # a checking acount 
    saving_account = SavingAccount(G.player_initial_money,env) # a saving account 
    player.set_bank_account(checking_account,saving_account)
    bank = Bank(player)

    print bank.loan_interest_rate(1)



