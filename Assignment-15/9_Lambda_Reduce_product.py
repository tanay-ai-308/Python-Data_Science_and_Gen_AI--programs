from functools import reduce

def main() :
	
	Lst = list()
	print("How many number you want to enter : ")
	No = int(input())

	print(f"Enter {No} number : ")
	for i in range(0,No,1):
		Lst.append(int(input()))

	Total = reduce(Product,Lst)

	print("Product of numbers is : ",Total)

Product = lambda No1,No2 : (No1*No2)

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

How many number you want to enter :
10
Enter 10 number :
1
2
3
4
5
6
7
8
9
10
Product of numbers is :  3628800

'''