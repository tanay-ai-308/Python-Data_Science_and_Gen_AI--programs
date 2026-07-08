from functools import reduce

def main() :

	NumList = list()

	print("How many number want to enter :- ")
	No = int(input())

	print(f"Enter {No} numbers :- ")
	for i in range(0,No,1) :
		NumList.append(int(input()))

	FData =list(filter(NumFilter,NumList))
	print("FData = ",FData)

	MData = list(map(Square,FData))
	print("MData = ",MData)

	Ret = reduce(Add,MData)
	print("Reduced output = ",Ret)

def NumFilter(No) :
	return (No%2 == 0)

def Square(No) :
	return No**2

def Add(No1,No2) :
	return No1+No2

if __name__ == '__main__':
	main()