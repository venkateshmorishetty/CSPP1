'''Assume s is a string of lower case characters.
Write a program that prints the longest substring
of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your
program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that
you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    '''it prints longest sequence'''
    string = input("enter string")
    count = len(string)
    i = 0
    string2 = ''
    string1 = ''
    while i <= count-2:
        if i == count-1:
            if string[i] > string[i-1]:
                string1 += string[i]
        elif string[i] <= string[i+1]:
            string1 += string[i]
        else:
            string1 += string[i]
            if len(string2) <= len(string1):
                string2 = string1
                string1 = ''
            else:
                string1 = ''
        i = i+1
    print(string2)
if __name__ == "__main__":
    main()
