'''Functions | Assignment-1 - Paying Debt off in a Year'''
# Write a program to calculate the credit card balance after one year
#if a person only pays the minimum monthly payment required by the
# credit card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
# balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
def paying_debtoff_inayear(balance, annualinterestrate, monthlypaymentrate):
    '''caluclate interest & balance'''
    month = 0
    while month < 12:
        monthlyinterestrate = (annualinterestrate) / 12.0
        minmonthlypayment = monthlypaymentrate * balance
        unpaid_balance = balance - minmonthlypayment
        balance = unpaid_balance + (unpaid_balance*monthlyinterestrate)
        month = month + 1
    print("Remaining balance:" +str(round(balance, 2)))

def main():
    '''credit card balance'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_debtoff_inayear(data[0], data[1], data[2])

if __name__ == "__main__":
    main()
