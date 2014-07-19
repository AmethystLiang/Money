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
    #parameter time has unit in month, and interest is counpounded by-weekly 
    #Loan interest rate also taken the player's credit into account. They higher the player credit,the lower the interest rate
    # see http://en.wikipedia.org/wiki/Compound_interest
    #t has to be at least a month
    def interest_rate(self,t,is_loan):
        P = 1000 # principle amount 
        S = 0 # value after time t 
        m = 2 # number of times the interest rate is compounded per month
        
        #calculating interest for a loan
        if is_loan:
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
        if self.balance >= amount :
            self.balance = self.balance - amount
        else :
            print "not enough money"
            return


    #to be implemented
    def report(self):
        pass
    

#add in the accout features so that characters can manage their money like in real life
class SavingAccount(Account):
    def __init__(self,initial_balance,env):
        Account.__init__(self,initial_balance,env)
        print " A saving account has been created for you"
        self.interest = 0  #initialize interest
        self.interest_rate = 0 #initialize interest rate


class CheckingAccount(Account):
    def __init__(self,initial_balance,env):
        Account.__init__(self,initial_balance,env)
        print " A checking account has been created for you"

    def withdraw_from_checking(self,amount):
        self.withdraw(amount) #use the money from checking account directly

if __name__ == '__main__':
    #test
    env = Environment()
    player = Player('Neil')
    checking_account = CheckingAccount(G.player_initial_money,env) # a checking acount 
    saving_account = SavingAccount(G.player_initial_money,env) # a saving account 
    player.set_bank_account(checking_account,saving_account)
    bank = Bank(player)

    print bank.interest_rate(1,True)



