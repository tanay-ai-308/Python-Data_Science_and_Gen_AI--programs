def main() :

	ListNum = list()

	print("Number of Elements :- ")
	No = int(input())

	print(f"Enter {No} Elements :- ")
	for i in range (0,No,1) :
		ListNum.append(int(input()))

	print("Enter a Number to Search : ")
	Key = int(input())

	Ret =  SearchKey(ListNum,Key)
	print(f"Frequency of {Key} is {Ret}.")

def SearchKey(Numbers ,Key) :

	Count = 0
	for No in Numbers :
		if (No == Key) :
			Count += 1

	return Count\

if __name__ == "__main__" :
	main ()