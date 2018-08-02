'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
	s = input()
	i=0
	temp=0
	length=len(s)
	string1=[]
	string2=[]
	while i<length-2:
		if s[i]<s[i+1]:
			string1.append(s[i])
			temp=temp+1
		else :
			if len(string1)>len(string2):
			 string2.append(string1)
			 string1=''	
		i=i+1		 
	print(string2)		 

	pass
if __name__== "__main__":
	main()
