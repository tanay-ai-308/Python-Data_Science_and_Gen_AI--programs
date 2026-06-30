def main() :
	
	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	Ret = ChkGreater(No1,No2)

	print("Greater number is : ",Ret)

def ChkGreater(No1 , No2) :

	if (No1>No2) :
		return No1
	else :
		return No2

if __name__ == "__main__" :
	main ()

'''
OUTPUT :- 

Enter first number :
13
Enter second number :
40
Greater number is :  40

'''