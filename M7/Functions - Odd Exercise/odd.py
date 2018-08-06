''' Exercise: odd'''

# Write a Python function, odd, that takes in
#one number and returns True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.


def odd(number):
    '''number checking'''
    return bool(number%2)
def main():
    '''returns true if it is odd else true'''
    data = input()
    print(odd(int(data)))
if __name__ == "__main__":
    main()
