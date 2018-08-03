'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''useing bisection method'''
    number = int(input())
    epsilon = 0.01
    high = number
    low = 0.0
    mid = (high+low)/2
    while abs(mid**2-number) >= epsilon:
        if mid**2 < number:
            low = mid
        else:
            high = mid
        mid = (high+low)/2
    print(mid)
if __name__ == "__main__":
    main()
