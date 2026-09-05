def main() :
	
	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	print("Enter thired number : ")
	No3 = int(input())

	Ret = ChkGreater(No1,No2,No3)

	print("Greater number is : ",Ret)

ChkGreater = lambda No1, No2, No3 : No1 if (No1>No2 and No1>No3) else No2 if (No2>No3) else No3

if __name__ == "__main__" :
	main ()

'''
OUTPUT :- 

Enter first number :
45
Enter second number :
12
Enter thired number :
43
Greater number is :  45

'''