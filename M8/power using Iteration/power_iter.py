# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    power=base
    if exp==0:
        power=1
    else:
        while exp!=1:
            power=base*power
            exp=exp-1    
    print(power)
    
def main():

    data = input()
    data = data.split()
    iterPower(float(data[0]),int(data[1])) 

if __name__== "__main__":
    main()