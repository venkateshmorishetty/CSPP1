''' Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	'''uses newton rapson method'''
	number = int(input())
	epsilon = 0.01
	guess=number/2.0
	while (guess**2-number)>=epsilon:
		guess=guess-(((guess**2)-number)/(2*guess))
	print(guess)	
if __name__== "__main__":
	main()
