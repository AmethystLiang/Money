""" a central location for parameters of the model."""
class G:
    player_initial_money = 500000
    maxTime =30 # days, namely,run for a week
    arrivalrate = 100 # per hour
    staytime = 2.0 # days
    customers = 0 #visited customers
    reported = 0 #represent the week that has been reported
    bankMoney = float("inf") #The money that a bank has. It's infinate
    intial_player_credit= 500 #........
    loan_interest_rate = 0.06  # monthlystated loan interest rate.
    save_interest_rate = 0.04  # monthlystated save interest rate.
    tillPay = 0  #time in unit of weeks representing how long it remains for you to pay back the loan
    tillWithdraw = 0 # time in unit of months representing how long it remains to take out money from saving account 
  