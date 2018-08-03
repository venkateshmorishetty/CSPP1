'''Write a python program to find the square root of the given number '''
# using approximation method

def main():
    '''print the square root'''
    number = int(input())
    '''taking ip'''
    guess = 0.0
    epsilon = 0.01
    increment = 0.1
    while abs(guess**2-number) >= epsilon:
        guess += increment
    if abs(guess**2-number) >= epsilon:
        print("not a square root")
    else:
        print(guess)
if __name__ == "__main__":
    main()
