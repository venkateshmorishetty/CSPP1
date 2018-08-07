'''Exercise: Assignment-1'''
# Write a Python function, factorial(n), that takes in one number
# and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(number):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if number == 0:
        return 1
    return number * factorial(number-1)
def main():
    '''takes input forward to factorial'''
    num = input()
    print(factorial(int(num)))
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(25500)
    main()
