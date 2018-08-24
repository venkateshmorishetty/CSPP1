'''tic tac'''
import copy
def tictac():
    '''tictac implementation'''
    rank1 = 0 #this rank is for o
    rank2 = 0 #this rank is for x
    t_t = []
    for _ in range(0, 3, 1):
        t_t += [input().split(' ')]
    count1 = 0
    count2 = 0
    for itemp in t_t:
        for jtemp in itemp:
            if jtemp not in ('o', 'x', '.'):
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
    for itemp in range(0, len(t_t), 1):
        list2 = []
        k = copy.deepcopy(t_t[itemp])
        temp = set(k)
        if len(temp) == 1:
            lis = list(temp)
            if lis[0] == 'o':
                rank1 = 1
            else:
                rank2 = 1
        lis = []
        k = []
        for jtemp in range(0, len(t_t[itemp]), 1):
            list2.append(t_t[jtemp][itemp])
            if itemp == jtemp:
                diag1.append(t_t[itemp][jtemp])
            if itemp + jtemp == len(t_t) - 1:
                diag2.append(t_t[itemp][jtemp])
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
