def main() :

	print("Enter Number :- ")
	No = int(input())

	Result = Table(No)

	print("Multiplication Table of ",No)
	print(Result)

def Table(No) :

	table = list()

	for i in range(1,11,1):
		table.append((i*No))

	return table

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter Number :-
5
Multiplication Table of  5
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

'''