import os
import multiprocessing

def main() :

	Elements = list()

	print("Enter how many numbers you want :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		Elements.append(int(input(f"Number {i} = ")))

	pObj = multiprocessing.Pool()
	Result = pObj.map(SumEven,Elements)
	pObj.close()
	pObj.join()

	print("\nResult numbers :- ")
	for i in range (0,No,1) :
		print(f"\t{Elements[i]} = {Result[i]}")

def SumEven(Number) :

	Sum = 0

	print("Process id = ",os.getpid())
	for i in range(1,Number+1,1) :
		if(ChkEven(i)) :
			Sum = Sum+i

	return Sum

def ChkEven(No) :

	if (No%2 == 0) :
		return 1
	else :
		return 0

if __name__ == "__main__" :
	main()