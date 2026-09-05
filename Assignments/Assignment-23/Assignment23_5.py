import time
import multiprocessing

def main() :

	Elements = list()

	print("Enter how many numbers you want :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		Elements.append(int(input(f"Number {i} = ")))

	startTime  = time.perf_counter()
	pObj = multiprocessing.Pool()
	Result = pObj.map(Power,Elements)
	pObj.close()
	pObj.join()
	endTime  = time.perf_counter()


	print("Total execution time = ",endTime-startTime)
	print("\nResult numbers :- ")
	for i in range (0,No,1) :
		print(f"\t{Elements[i]} = {Result[i]}")

def Power(Number) :

	Sum = 0

	for i in range(1,Number+1,1) :
		Sum = Sum + (i**5)

	return Sum

if __name__ == "__main__" :
	main()