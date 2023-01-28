#first import sring and random module
import string
import random
if __name__==("__main__"):
	A=string.ascii_uppercase
	a=string.ascii_lowercase
	d=string.digits
	p=string.punctuation
	
	password=int(input("enter length"))
	#now make a empty list
	lis=[]
	# now extend sting in list
	lis.extend(list(A))
	lis.extend(list(a))
	lis.extend(list(d))
	lis.extend(list(p))
	
	#use random module shuffle
	random.shuffle(lis)
	
	print("".join(lis[0:password]))
	