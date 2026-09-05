def main() :

	ListNum = list()

	print("Number of Elements :- ")
	No = int(input())

	print(f"Enter {No} Elements :- ")
	for i in range (0,No,1) :
		ListNum.append(int(input()))

	Ret = Maximum(ListNum)

	print(f"Maximum from given numbers is {Ret}.")

def Maximum(Numbers) :

	Max = 0

	for No in Numbers :
		if (No>Max) :
			Max = No

	return Max

if __name__ == "__main__" :
	main ()