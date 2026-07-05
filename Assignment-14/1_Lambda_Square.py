def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = Square(No)

	print("Sqaure of number is : ",Ret)

Square = lambda No : (No*No)

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter number :
12
Sqaure of number is :  144

'''