'''Exercise : Odd Tuples'''
#Write a python function oddTuples(aTup)
#that takes a some numbers in the tuple as input and returns a tuple
#in which contains odd index values in the input tuple
def oddtuples(atup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    new = atup[0::2]
    return new
def main():
    '''takes tuple and forwards it to oddTuples'''
    data = input()
    data = data.split()
    atup = ()
    for j in data:
        atup += (j,)
    print(oddtuples(atup))
if __name__ == "__main__":
    main()
