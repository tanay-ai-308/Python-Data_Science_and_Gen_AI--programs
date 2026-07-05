def main() :
	
	Lst = list()
	print("How many number you want to enter : ")
	No = int(input())

	print(f"Enter {No} number : ")
	for i in range(0,No,1):
		Lst.append(int(input()))

	FData = len(list(filter(CountEven,Lst)))

	print("Total even numbers are : ",FData)

CountEven = lambda No1 : True if (No1%2 == 0) else False

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
Total even numbers are : 5

'''