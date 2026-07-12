import os
import multiprocessing

def main() :

	Elements = list()

	print("Enter how many numbers you want :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		Elements.append(int(input(f"Number {i} = ")))

	pObj = multiprocessing.Pool()
	Result = pObj.map(Prime,Elements)
	pObj.close()
	pObj.join()

	print("\nPrime numbers :- ")
	for i in range (0,No,1) :
		print(f"\t{Elements[i]} = {Result[i]}")

def Prime(Number) :

	Count = 0

	for i in range(2,Number+1,1) :
		if(CheckPrime(i)):
			Count += 1

	return Count

def CheckPrime(No) :

	if (No<=1) :
		return 0
	else :
		for i in range (2,No,1) :
			if (No%i == 0) :
				return 0

		return 1

if __name__ == "__main__" :
	main()