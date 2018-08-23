import copy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mul = []
    for i in range(len(m1)):
        m=[]
        for j in range(len(m2[0])):
            res = 0
            for k in range(len(m2)):
                res += int(m1[i][k])*int(m2[k][j])
            m.append(res)
        mul.append(m)        
    return mul            
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    n1 = len(m1)
    n2 = len(m2)
    if n1 != n2:
        print("Error: Matrix shapes invalid for addition")
        return None
    else:
        add = copy.deepcopy(m1)
        for i in range(0,n2,1):
            for j in range(0,len(m2[i]),1):
                add[i][j] = int(add[i][j])
                add[i][j] += int(m2[i][j])    
        return add        


def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    # print(size)
    # print(size[0])
    # print(size[1])
    rows = int(size[0])
    cols = int(size[1])
    total = 0
    matrix = []
    for i in range(0,rows,1):
        row = input().split( )
        matrix.append(row)
        total += len(row)   
    return matrix,total       
    

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    n1 = input().split(',')
    matrix1,total1 = read_matrix(n1)
    n2 = input().split(',')
    matrix2,total2 = read_matrix(n2)
    if total1 != total2:
        print("Error: Invalid input for the matrix")
    else:
        print(add_matrix(matrix1,matrix2))
        if n1[1] != n2[0]:
            print("Error: Matrix shapes invalid for mult")

        else:        
            print(mult_matrix(matrix1,matrix2))

if __name__ == '__main__':
    main()
