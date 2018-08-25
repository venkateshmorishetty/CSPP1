'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    '''read text strores in string'''
    num = int(input())
    string1 = ''
    for _ in range(0, num, 1):
        string1 += str(input()) + "\n"
    print(string1)
if __name__ == '__main__':
    main()
