'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
dic = {}

def tokenize(string):
	# string1 = re.sub('[^a-zA-Z0-9]','',string)
	
	list1 = string.split(' ')
	for index in list1:
		index1 = re.sub('[^a-zA-Z0-9]','',index)
		if index1 in dic:
			dic[index1] += 1
		else:
			dic[index1] = 1
				

    
            
def main():
    n = int(input())
    for index in range(0, n, 1):
    	string = input()
    	tokenize(string)
    print(dic)	

if __name__ == '__main__':
    main()
