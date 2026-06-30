def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = Square(No)

	print("Sqaure of number is : ",Ret)

def Square(No) :
	return No*No

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter number :
12
Sqaure of number is :  144

'''