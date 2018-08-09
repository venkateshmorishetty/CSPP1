'''Exercise : Biggest Exercise'''
#Write a procedure, called biggest, which returns
#the key corresponding to the entry with the largest number of values associated with it.
#If there is more than one such entry, return any one of the matching keys.


def biggest(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    string = adict.values()
    length = 0
    for index1 in string:
        if len(index1) > length:
            length = len(index1)
    for index2 in adict:
        count = len(adict[index2])
        if count == length:
            result = index2
            break
    return result
def main():
    '''Biggest Exercise'''
    adict = {}
    number = input()
    for _ in range(int(number)):
        string = input()
        last = string.split()
        if last[0][0] not in adict:
            adict[last[0][0]] = [last[1]]
        else:
            adict[last[0][0]].append(last[1])

    print(biggest(adict))
if __name__ == "__main__":
    main()
