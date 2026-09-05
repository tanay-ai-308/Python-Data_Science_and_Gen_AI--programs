import MarvellousNum

def main ():

	ListNum = list()

	print("Number of Elements :- ")
	No = int(input())

	print(f"Enter {No} Elements :- ")
	for i in range (0,No,1) :
		ListNum.append(int(input()))

	SumPrime = ListPrime(ListNum)

	print("Sum of all prime numbers from list is : ",SumPrime)
	
def ListPrime(Numbers) :

	Sum = 0

	for No in Numbers :
		if(MarvellousNum.ChkPrime(No)) :
			Sum = Sum+No

	return Sum
if __name__ == "__main__" :
	main ()