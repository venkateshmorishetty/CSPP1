'''Assignment-2 - Paying Debt off in a Year'''

# Now write a program that calculates the minimum fixed monthly payment
# needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change
# each month, but instead is a constant amount that will be
# paid each month.
#the balance at the end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)

def payingdebtoffinayear(balance, annualinterestrate):
    '''finds minimum monthly payment rate'''
    monthlyinterestrate = annualinterestrate/12
    minimummonthlypayment = 10
    bal = balance
    while balance > 0:
        monthlyunpaidbalance = bal
        month = 12
        while month != 0:
            monthlyunpaidbalance = monthlyunpaidbalance - minimummonthlypayment
            cmi = monthlyunpaidbalance*monthlyinterestrate
            monthlyunpaidbalance = monthlyunpaidbalance+cmi
            month -= 1
        balance = monthlyunpaidbalance
        minimummonthlypayment += 10
    print(minimummonthlypayment - 10)
def main():
    '''main'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffinayear(data[0], data[1]))
if __name__ == "__main__":
    main()
