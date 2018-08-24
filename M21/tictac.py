import copy
def tictac():
    r1 = 0 #=====o
    r2 = 0 #=====x
    n = []
    for i in range(0,3,1):
        n += [input().split(' ')]
    # print(n)
    for i in n:
        for j in i:
            if j != 'o' and j != 'x' and j != '.':
                return "invalid game"

    
    diag1 = []
    diag2 = []
    matrix2 = []    
    for i in range(len(n)):
        l2 = []
        k = copy.deepcopy(n[i])
        temp = set(k)
        if len(temp) ==1:
            l = list(temp)
            if l[0] == 'o':
                r1 =1
            else:
                r2 =1
        l = []
        k = []      
        for j in range(len(n[i])):
            l2.append(n[j][i])      
            if i == j:
                diag1.append(n[i][j])
            if i+j==len(n)-1:
                diag2.append(n[i][j])
        matrix2.append(l2)      
    # print("matrix2",matrix2)          
    for i in range(len(matrix2)):
        k = copy.deepcopy(matrix2[i])
        temp = set(k)
        if len(temp) ==1:
            l = list(temp)
            if l[0] == 'o':
                r1 =1
            elif l[0] == 'x':
                r2 =1
    # print("after transpose",r1)
    # print("after transpose",r2)           

                                                
    temp = set(diag1)
    if len(temp) == 1:
        l = list(temp)
        if l[0] == 'o':
            r1 = 2
        else:
            r2 = 2      
    temp = set()        
    temp = set(diag2)
    if len(temp) == 1:
        l = list(temp)
        if l[0] == 'o':
            r1 = 2
        else:
            r2 = 2

    # print(r1)
    # print(r2)         
    if r1>r2:
        return 'o'
    if r1==r2:
        return "draw"
    else:
        return 'x'






def main():
    print(tictac())

if __name__ == "__main__":
    main()