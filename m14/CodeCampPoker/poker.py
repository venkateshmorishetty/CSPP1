'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
maximum={}
adic = {}
def dictonary(rank,hand):
    if rank not in adic:
        adic[rank] = [hand]
    else:
        adic[rank].append(hand)    
    #print("adic is",adic)
def list1(hand):
    '''add t,j,q,k values in this function to list'''
    new = []
    for j in hand:
        k = list(j)
        if k[0] == 'T':
            new.append(10)
        elif k[0] == 'J':
            new.append(11)
        elif k[0] == 'Q':
            new.append(12)
        elif k[0] == 'K':
            new.append(13)
        elif k[0] == 'A':
            new.append(14)
        else:
            new.append(k[0])
    new = list(map(int, new))
    return new
def ranks(hand):
    '''returns count of each value in list'''
    new = list1(hand)
    counter = []
    j = 0
    new1 = new.copy()
    while j < len(new):
        temp = new[j]
        count = 0
        for i in new1:
            if temp == i:
                count += 1
        counter.append(count)
        j += 1
    return counter
def is_twopair(hands):
    '''checks whether list is two_pair'''
    rank = ranks(hands)
    count = rank.count(2)
    if count == 4:
        return True
    return False
def is_onepair(hands):
    '''checks whether list is onepair'''
    rank = ranks(hands)
    if max(rank) == 2:
        return True
    return False 
def is_fourkind(hands):
    '''checks is list is four kind'''
    rank = ranks(hands)
    if max(rank) == 4:
        return True
    return False    
def is_threekind(hands):
    '''checks is list is three kind'''
    rank = ranks(hands)
    if max(rank) == 3:
        return True
    return False    
def fullhouse(hands):
    '''checks is list is full house'''
    rank = ranks(hands)
    if 3 in rank:
        if 2 in rank:
            return True
    return False                       
def high_card(hands):
    hands1=list1(hands)
    temp1 = max(hands1)
    if temp1 not in maximum:
        maximum[temp1]=hands
    # print(maximum)    
    # print(maximum[max(maximum)])
    #print("it is",max(maximum))
    return max(maximum)/100
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    new = list1(hand)
    new.sort()
    for j in range(len(new)-1):
        if j == len(new):
            break
        elif new[j+1]-new[j] == 1:
            continue
        else:
            return False
    return True
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    new = []
    for j in hand:
        k = list(j)
        new += k[1]
    temp = new[0]
    for j in new:
        k = j
        if temp == k:
            continue
        else:
            return False
    return True
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # # max in poker function uses these return values to select the best hand
    if fullhouse(hand):
        dictonary(7,hand)
        return 7
    if is_twopair(hand):
        dictonary(2,hand)
        return 2
    if is_onepair(hand):
        dictonary(1,hand)
        return 1
    if is_threekind(hand):
        dictonary(3,hand)
        return 3
    if is_fourkind(hand):
        dictonary(4,hand)
        return 4
    if is_flush(hand) and is_straight(hand):
        dictonary(8,hand)
        return 8
    if is_straight(hand):
        dictonary(5,hand)
        return 5
    if is_flush(hand):
        dictonary(6,hand)
        return 6
    return high_card(hand)
    return 0    
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    