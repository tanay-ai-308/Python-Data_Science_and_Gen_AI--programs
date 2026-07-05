def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = ChkDivisible_5(No)

	print(Ret)

ChkDivisible_5 = lambda No1 : True if (No1%5 == 0) else False

if __name__ == "__main__" :
	main ()

'''
OUTPUT :- 

Enter number :
12
True

'''