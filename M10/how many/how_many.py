'''Exercise : how many'''
# write a procedure, called how_many which returns
#the sum of the number of values associated with a dictionary.
def how_many(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    values = []
    values = adict.values()
    for index in values:
        result = result+len(index)
    return result
def main():
    '''main function'''
    adict = {}
    number = input()
    for _ in range(int(number)):
        string = input()
        last = string.split()
        if last[0][0] not in adict:
            adict[last[0][0]] = [last[1]]
        else:
            adict[last[0][0]].append(last[1])
    print(how_many(adict))
if __name__ == "__main__":
    main()
