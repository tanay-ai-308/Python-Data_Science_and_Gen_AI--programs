import os
import multiprocessing

def main() :

	Elements = list()

	print("Enter how many numbers you want :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		Elements.append(int(input(f"Number {i} = ")))

	pObj = multiprocessing.Pool()
	Result = pObj.map(Factorial,Elements)
	pObj.close()
	pObj.join()

	print("\nFactorial of given number :- ")
	for i in range (0,No,1) :
		print(f"\t{Elements[i]}! = {Result[i]}")

def Factorial(Number) :

	Sum = 1

	print("Process id = ",os.getpid())
	for i in range(1,Number+1,1) :
		Sum = Sum * i

	return Sum

if __name__ == "__main__" :
	main()