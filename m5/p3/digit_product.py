'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    num = int(input())
    flag = 0
    mul = 1
    if num == 0:
        print(0)
    else:
        if num < 0:
            number = abs(num)
            flag = 1
        else:
            number = num
        while number != 0:
            digit = number%10
            mul = mul*digit
            number = number//10
        if flag == 1:
            print(-mul)
        else:
            print(mul)
if __name__ == "__main__":
    main()
