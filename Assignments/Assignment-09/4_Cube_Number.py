def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = Cube(No)

	print("Cube of number is : ",Ret)

def Cube(No) :
	return (No*No*No)

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter number :
3
Cube of number is :  27

'''