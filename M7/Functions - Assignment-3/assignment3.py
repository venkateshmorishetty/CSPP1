'''Functions - Assignment-3 - Using Bisection Search to Make the Program Faster'''
def cal(month, balance, mid, monthlyinterestrate):
    '''caluclate mid for each year'''
    while month <= 12:
        monthlyunpaidbalance = balance - mid
        balance = monthlyunpaidbalance + (monthlyinterestrate * monthlyunpaidbalance)
        month += 1
    return balance
def payingdebtoffinayear(balance, annualinterestrate):
    '''returns mid'''
    bal = balance
    monthlyinterestrate = annualinterestrate / 12.0
    mlb = balance / 12
    mub = (balance * ((1 + monthlyinterestrate) ** 12)) / 12.0
    mid = (mlb + mub) / 2.0
    epsilon = 0.0001
    month = 0
    while abs(balance) >= epsilon:
        balance = bal
        month = 0
        balance = cal(month, balance, mid, monthlyinterestrate)
        if balance > 0:
            mlb = mid
        else:
            mub = mid
        mid = (mlb + mub) / 2.0
    return str(round(mid, 2))
def main():
    '''Using Bisection Search to Make the Program Faster'''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", payingdebtoffinayear(data[0], data[1]))
if __name__ == "__main__":
    main()
