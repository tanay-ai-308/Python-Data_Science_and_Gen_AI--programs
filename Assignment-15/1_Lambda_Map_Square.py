def main() :
	
	Lst = list()
	print("How many number you want to enter : ")
	No = int(input())

	print(f"Enter {No} number : ")
	for i in range(0,No,1):
		Lst.append(int(input()))

	MData = list (map(Square,Lst))

	print("Sqaure of numbers is : ",MData)

Square = lambda No : (No*No)

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

How many number you want to enter :
4
Enter 4 number :
12
13
14
15
Sqaure of numbers is :  [144, 169, 196, 225]

'''