'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    num = int(input())
    string1 = ''
    for index in range(0,num,1):
    	string1 += str(input()) + "\n"
    
    print(string1)



if __name__ == '__main__':
    main()
