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
    string = input()
    count = len(string)
    i = 0
    j = 0
    t1 = 0
    t2 = 0
    while i < count-1:
        if string[i] <= string[i+1]:
            t1 += 1
            if t1 > t2:
                t2 = t1
                j = i+1
            else:
                t1 = 0
            i += 1
    string1 = j-t2
    print(string1[string:j+1])
if __name__ == "__main__":
    main()
