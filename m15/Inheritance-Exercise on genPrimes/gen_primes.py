#define the gen_primes function here
def genPrimes():
	temp = 2
	while temp>0:
		prime = True
		for i in range(2,temp,1):
			if temp%i == 0:
				prime = False
		if prime:
			yield temp
		temp += 1			
def main():
	data = input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.__next__()
	    if(i%b==0):
	        print(p)
	
if __name__== "__main__":
	main()
