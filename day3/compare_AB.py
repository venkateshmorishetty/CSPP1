varA=int(input("enter value1 "))
varB=int(input("enter value2 "))
if type(varA)==str or type(varB)==str:
	print("strings involved")
elif varA>varB:
	print("bigger")
else:
	print("smaller")
