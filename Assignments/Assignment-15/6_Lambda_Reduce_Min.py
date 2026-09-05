from functools import reduce

def main() :
	
	Lst = list()
	print("How many number you want to enter : ")
	No = int(input())

	print(f"Enter {No} number : ")
	for i in range(0,No,1):
		Lst.append(int(input()))

	Min = reduce(Minimum,Lst)

	print("Minimum number is : ",Min)

Minimum = lambda No1, No2 : No1 if (No1<No2) else No2

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

How many number you want to enter :
12
Enter 12 number :
23
34
86
96
46
84
41
86
357
86
53
840
Minimum number is :  23

'''