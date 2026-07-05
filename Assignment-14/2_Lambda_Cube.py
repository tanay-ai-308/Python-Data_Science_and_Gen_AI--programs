def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = Square(No)

	print("Cube of number is : ",Ret)

Square = lambda No : (No*No*No)

if __name__ == "__main__" :
	main ()