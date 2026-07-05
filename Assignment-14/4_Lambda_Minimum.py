def main() :
	
	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	Ret = ChkLesser(No1,No2)

	print("Smallest number is : ",Ret)

ChkLesser = lambda No1, No2 : No1 if (No1<No2) else No2

if __name__ == "__main__" :
	main ()

'''
OUTPUT :- 

Enter first number :
13
Enter second number :
40
Smallest number is :  13

'''