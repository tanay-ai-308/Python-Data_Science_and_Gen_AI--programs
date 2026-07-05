def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = ChkEven(No)

	print(Ret)

ChkEven = lambda No1 : True if (No1%2 == 0) else False

if __name__ == "__main__" :
	main ()

'''
OUTPUT :- 

Enter number :
12
True

'''