'''matrix multiploication and addition'''
import copy
def mult_matrix(matrix1, matrix2, temp1, temp2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if temp1 != temp2:
        print("Error: Matrix shapes invalid for mult")
        return None
    mul = []
    for itemp in range(len(matrix1)):
        temp = []
        for jtemp in range(len(matrix2[0])):
            res = 0
            for ktemp in range(len(matrix2)):
                res += int(matrix1[itemp][ktemp])*int(matrix2[ktemp][jtemp])
            temp.append(res)
        mul.append(temp)
    return mul
def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    length1 = len(matrix1)
    length2 = len(matrix2)
    if length1 != length2:
        print("Error: Matrix shapes invalid for addition")
        return None
    add = copy.deepcopy(matrix1)
    for itemp in range(0, length2, 1):
        for jtemp in range(0, len(matrix2[itemp]), 1):
            add[itemp][jtemp] = int(add[itemp][jtemp])
            add[itemp][jtemp] += int(matrix2[itemp][jtemp])
    return add
def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    total = 0
    matrix = []
    val1 = int(size[0])
    for _ in range(0, val1, 1):
        row = input().split()
        matrix.append(row)
        total += len(row)
    return matrix, total
def main():
    '''read matrix 1,read matrix 2,
    add matrix 1 and matrix 2
    multiply matrix 1 and matrix 2'''
    size1 = input().split(',')
    matrix1, total1 = read_matrix(size1)
    size2 = input().split(',')
    matrix2, total2 = read_matrix(size2)
    if total1 != total2:
        print("Error: Invalid input for the matrix")
    else:
        print(add_matrix(matrix1, matrix2))
        print(mult_matrix(matrix1, matrix2, size1[1], size2[0]))
if __name__ == '__main__':
    main()
