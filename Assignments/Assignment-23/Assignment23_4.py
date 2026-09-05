import os
import multiprocessing

def main() :

	Elements = list()

	print("Enter how many numbers you want :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		Elements.append(int(input(f"Number {i} = ")))

	pObj = multiprocessing.Pool()
	Result = pObj.map(SumOdd,Elements)
	pObj.close()
	pObj.join()

	print("\nResult numbers :- ")
	for i in range (0,No,1) :
		print(f"\t{Elements[i]} = {Result[i]}")

def SumOdd(Number) :

	Count = 0

	print("Process id = ",os.getpid())
	for i in range(1,Number+1,1) :
		if(ChkOdd(i)) :
			Count = Count+1

	return Count

def ChkOdd(No) :

	if (No%2 == 0) :
		return 0
	else :
		return 1

if __name__ == "__main__" :
	main()