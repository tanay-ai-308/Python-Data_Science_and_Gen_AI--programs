import multiprocessing

def main() :

	Elements = list()

	print("Enter how many numbers you want :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		Elements.append(int(input(f"Number {i} = ")))

	pObj = multiprocessing.Pool()
	Result = pObj.map(Square,Elements)
	pObj.close()
	pObj.join()

	print("Result = ",Result)

def Square(Number) :

	Sum = 0

	for i in range(1,Number+1,1) :
		Sum = Sum + (i**2)

	return Sum

if __name__ == "__main__" :
	main()