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

	MData = list(map(Multiply,FData))
	print("MData = ",MData)

	Ret = reduce(Maximum,MData)
	print("Reduced output = ",Ret)

def NumFilter(No) :
	if (No<=1) :
		return 0
	else :
		for i in range (2,No,1) :
			if (No%i == 0) :
				return 0

		return 1

def Multiply(No) :
	return No*2

def Maximum(No1,No2) :
	if(No1>No2):
		return No1

	return No2

if __name__ == '__main__':
	main()