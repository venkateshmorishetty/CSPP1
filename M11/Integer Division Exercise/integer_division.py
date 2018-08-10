'''Exercise: Integer Division Exercise'''
#Modify the code for integer_division so that this error does not occur.

def integer_division(num1, num2):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while num1 >= num2:
        count += 1
        num1 = num1 - num2
    return count
def main():
    '''Exercise: Integer Division Exercise'''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
