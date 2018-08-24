'''tic tac'''
import copy
def tictac():
    '''tictac implementation'''
    rank1 = 0 #this rank is for o
    rank2 = 0 #this rank is for x
    tt = []
    for i in range(0, 3, 1):
        tt += [input().split(' ')]
    count1 = 0
    count2 = 0
    for itemp in tt:
        for jtemp in itemp:
            if jtemp != 'o' and jtemp != 'x' and jtemp != '.':
                return "invalid input"
            if jtemp == 'o':
                count1 += 1
            if jtemp == 'x':
                count2 += 1
    if abs(count1 - count2) != 1:
        return "invalid game"
    diag1 = []
    diag2 = []
    matrix2 = []
    for itemp in range(0, len(tt), 1):
        list2 = []
        k = copy.deepcopy(tt[itemp])
        temp = set(k)
        if len(temp) == 1:
            lis = list(temp)
            if lis[0] == 'o':
                rank1 = 1
            else:
                rank2 = 1
        lis = []
        k = []
        for jtemp in range(0, len(tt[itemp]), 1):
            list2.append(tt[jtemp][itemp])
            if itemp == jtemp:
                diag1.append(tt[itemp][jtemp])
            if itemp + jtemp == len(tt) - 1:
                diag2.append(tt[itemp][jtemp])
        matrix2.append(list2)
    for itemp in range(0, len(matrix2), 1):
        k = copy.deepcopy(matrix2[itemp])
        temp = set(k)
        if len(temp) == 1:
            lis = list(temp)
            if lis[0] == 'o':
                rank1 = 1
            elif lis[0] == 'x':
                rank2 = 1
    temp = set(diag1)
    if len(temp) == 1:
        lis = list(temp)
        if lis[0] == 'o':
            rank1 = 2
        else:
            rank2 = 2
    temp = set()
    temp = set(diag2)
    if len(temp) == 1:
        lis = list(temp)
        if lis[0] == 'o':
            rank1 = 2
        else:
            rank2 = 2
    if rank1 > rank2:
        return 'o'
    if rank1 == rank2:
        return "draw"
    return 'x'
def main():
    '''mainfunction calls the tictac function'''
    print(tictac())
if __name__ == "__main__":
    main()
