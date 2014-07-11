from __future__ import division  # to allow fraction division
from simpy import *
from Customer import *
from Bank import *
from Player import *
from GlobalDeclaration import *
from Tools import *

class BankController():
    """This bank simulates a bank. Customers can go into the bank and carry out transactions"""
    def __init__(self, env, player):
        self.env = env
        self.player = player
        self.bank = 0


        #todo : add in save money part

    def setup(self):
        checking_account = CheckingAccount(G.player_initial_money,self.env) # a checking acount 
        saving_account = SavingAccount(G.player_initial_money,self.env) # a saving account 
        self.player.set_bank_account(checking_account,saving_account) #give the above accounts to the player
        self.bank = Bank(player) #set up the bank

    def withdraw_from_checking(player,amount):
        player.checking_account.withdraw(amount) #use the money from checking account directly


    def checking_to_saving(self):
        print "You're transfering money from your checking account to your saving account. "
        while True: 
            time = check_positive_valid_input("Please enter the time you keep money in your saving account? Units are in months."+'\n'\
                +"Please note you can't loan money for less than a month")
            if not (time/1 <1 ):
                break
            print "Please enter a valid input."   
        interest_rate = self.bank.interest_rate(time,False)
        print "The interest rate for your saving is %.5f " %interest_rate  #print out 5 effective digits
        wanna_save = check_confirm("Print Y to continue your transfering money to your saving account with above interest rate. Press N to exit.") 
        if wanna_save : 
            amount = self.bank.money  #initialize amount to enter 
            while amount > self.bank.checking_account.balance : 
                amount = check_positive_valid_input("Please enter the amount you want to loan from the bank ? ")
                if amount < self.bank.checking_account.balance:
                    break
                print "Please enter the right input."
            self.bank.checking_account..withdraw(amount) #first, withdraw the money from checkign account
            self.bank.saving_account.save(amount) #then put it in saving account 
            G.tillWithdraw = time   #set the countdown
            self.bank.interest = amount * interest_rate
        else : 
            return

    def saving_to_checking (self):
        if G.tillWithdraw != 0:
            print "You have to wait %d months to get interest from your saving. " %G.tillWithdraw
            go_on = check_confirm("Enter Y to continue transferming money to checking without any interest. Enter N to stop.")
            if not go_on :
                return
            self.bank.interest = 0
        to_checking = self.bank.saving_account.balance + self.bank.interest   #initial money plus interest 
        self.bank.saving_account..withdraw(self.bank.saving_account.balance) #first, withdraw the money from saving account
        self.bank.checking_account.save(to_checking) #then put it in checking account 



    def loan(self):
        time = 0
        while True: 
            time = check_positive_valid_input("Please enter the time you want keep this loan? Units are in months."+'\n'\
                +"Please note you can't loan money for less than a month")
            if not (time/1 <1 ):
                break
            print "Please enter a valid input."   
        interest_rate = self.bank.interest_rate(time,True)
        print "Your personal credit is %d" %self.player.credit
        print "The interest rate for your loan is %.5f " %interest_rate  #print out 5 effective digits
        wanna_loan = check_confirm("Print Y to continue your loan application with above interest rate. Press N to exit.")
        if wanna_loan : 
            amount = check_positive_valid_input("Please enter the amount you want to loan from the bank ? ")
            G.tillpay = time*4 #set the countdown to pay the money 
            self.player.loan = amount
            slef.bank.checking_account.save(amount) #transfer the money to player's checking account
            print "Sucessfully borrow %d dollars from the bank. You have to pay it back" %amount
        else : 
            return


    def pay_loan(self):
        if not (self.bank.checking_account.balance<self.player.loan ) :
            print "Paying back all the %d dollars loan using your checking account " %self.player.loan
            self.bank.checking_account.withdraw(self.player.loan )  #pay back the loan by withdrawing money from checking account
            return
        if not (self.bank.checking_account.balance + self.bank.saving_account.balance < self.player.loan ):
            print "Paying back the %d dollars of your totoal %d loan using your checking account. " %(self.bank.checking_account,self.player.loan) 
            self.bank.checking_account.withdraw(self.bank.checking_account.balance) #first, use all money in checking account 
            print "Paying back the remaining %d dollars of loan using your saving account. " %(self.player.loan) 
            self.bank.loan  -= self.bank.checking_account.balance  #deduct the paid part from self.player.loan 
            self.bank.saving_account.withdraw(self.bank.loan ) # next, pay the rest of the money using the money in saving account
            return
        #has not enough money to pay.
        else :
            orginial_loan = self.player.loan
            print "Paying back the %d dollars of your totoal %d loan using your checking account. " %(self.bank.checking_account.balance,self.player.loan) 
            self.player.loan  -= self.bank.checking_account.balance #deduct the paid part from self.player.loan 
            self.player.checking_account.withdraw(self.player.checking_account.balance) #first, use all money in checking account 
            print "Paying back the %d dollars of the remaining %d loan using your saving account. " %(self.bank.saving_account.balance,self.player.loan) 
            self.player.loan -= self.bank.saving_account.balance  #deduct the paid part from self.player.loan 
            self.bank.saving_account.withdraw(self.bank.saving_account_balance)# next, pay the rest of the money using the money in saving account
            deduct = 100*(self.player.loan/orginial_loan)
            print "You don't have enough money to pay back your loan. As a result, we deduct %d points from your credit points") %deduct
            self.player.credit -= deduct   #deduct credit based on how much you couldn't repaly

        
        def check_checking_balance(self):
            print "Your checking account balance is %d dollars. " %self.bank.checking_account.balance 


        def check_saving_balance(self):
            print "Your saving account balance is %d dollars. " %self.bank.saving_account.balance       
        







if __name__ == '__main__':
    env = Environment()
    player = Player('Neil')
    bc = BankController(env,player)
    bc.setup()
    bc.loan()

    

    