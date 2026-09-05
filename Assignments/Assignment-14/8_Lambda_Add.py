def main() :
	
	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	Ret = Add(No1,No2)

	print("Addition is number is : ",Ret)

Add = lambda No1, No2 : No1+No2 

if __name__ == "__main__" :
	main ()

'''
OUTPUT :- 

Enter first number :
13
Enter second number :
40
Addition is number is :  53

'''