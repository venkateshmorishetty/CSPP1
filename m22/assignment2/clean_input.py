'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''filters the string'''
    result = re.sub('[^a-zA-Z0-9]', '', string)
    return result
def main():
    '''read input and pass it to clan_string.'''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
