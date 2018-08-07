# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    high=len(aStr)-1
    low=0
    mid=(high+low)//2
    if char==aStr[mid]:
        return True 
    else:
        if aStr[mid]>char:
            aStr=aStr[0:mid-1]
            isIn(char,aStr)
            high=mid-1
            low=0
        else:
            aStr=aStr[mid+1:high]
            isIn(char,aStr)
            high=high
            low=mid+1        
            
   

def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__== "__main__":
    main()