'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
dictionary = {}
def tokenize(string):
    '''tokenize'''
    # string1 = re.sub('[^a-zA-Z0-9]','',string)
    list1 = string.split(' ')
    for index_ in list1:
        index1 = re.sub('[^a-zA-Z0-9]', '', index_)
        if index1 in dictionary:
            dictionary[index1] += 1
        else:
            dictionary[index1] = 1
def main():
    '''main'''
    lines = int(input())
    for _ in range(0, lines, 1):
        string = input()
        tokenize(string)
    print(dictionary)
if __name__ == '__main__':
    main()
