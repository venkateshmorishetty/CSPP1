'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def find_bob(string, index):
    return string.find("bob", index)

def main():
    ''' This function finds the number of occurances of bob'''
    string = input()
    # the input string is in s
    # remove pass and start your code here
    index = find_bob(string, 0)
    count = 0
    while index > 0:
        print(index)
        count += 1
        index = find_bob(string, index+1)
    print(count)

if __name__ == "__main__":
    main()
