def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = ChkOdd(No)

	print(Ret)

ChkOdd = lambda No1 : True if (No1%2 == 1) else False

if __name__ == "__main__" :
	main ()

'''
OUTPUT :- 

Enter number :
13
True

'''