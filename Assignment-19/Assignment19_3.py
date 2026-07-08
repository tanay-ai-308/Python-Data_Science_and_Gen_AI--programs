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

	MData = list(map(Increment,FData))
	print("MData = ",MData)

	Ret = reduce(Product,MData)
	print("Reduced output = ",Ret)

def NumFilter(No) :
	return (No<=90 and No>=70)

def Increment(No) :
	return No+10

def Product(No1,No2) :
	return No1*No2

if __name__ == '__main__':
	main()