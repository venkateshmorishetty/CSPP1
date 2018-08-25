'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
import copy            
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    sum1 =0
    for i in sudoku:
        for j in i:
            sum1 += int(j)
        if sum1!=45:
            return  False
        else:
            sum1 = 0            
            
               
    transpose = copy.deepcopy(sudoku)        
    for i in range(0,len(sudoku),1):
        for j in range(len(sudoku[0])):
            transpose[i][j] = int(sudoku[j][i])
    sum2 = 0            
    for i in transpose:
        for j in i:
            sum2 += int(j)
        if sum2 != 45:
            return False
        else:
            sum2 = 0     
    sum3 = []
    temp = 0
    # for i in range(0,9,1):
    #     for j in range(0,9,1):
    #         if i in (0,1,2) and j in (0,1,2):
    #             temp += int(sudoku[i][j])
    #     sum3.append(temp)              
    #         if i in (0,1,2) and j in (3,4,5):
    #             temp += int(sudoku[i][j])
    #     sum3.append(temp)
    #     temp = 0
    #         if i in (0,1,2) and j in (6,7,8):
    #             temp += int(sudoku[i][j])
    #     ṇsum3.append(temp)
            
    # print(sum3)


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()