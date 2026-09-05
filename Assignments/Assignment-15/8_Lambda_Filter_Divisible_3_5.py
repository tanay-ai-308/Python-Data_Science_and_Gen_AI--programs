def main() :
	
	Lst = list()
	print("How many number you want to enter : ")
	No = int(input())

	print(f"Enter {No} number : ")
	for i in range(0,No,1):
		Lst.append(int(input()))

	FData = list (filter(Divisible3_5,Lst))

	print("Numbers Divisible by 3 and 5 are : ",FData)

Divisible3_5 = lambda No : No if (No%3 == 0 and No%5 == 0) else None

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

How many number you want to enter :
12
Enter 12 number :
12
13
15
3
45
5
10
20
30
60
75
34
Numbers Divisible by 3 and 5 are :  [15, 45, 30, 60, 75]

'''