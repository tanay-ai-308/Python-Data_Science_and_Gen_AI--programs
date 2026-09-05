def main() :

	print("Enter a number :- ")
	No = int(input())

	Ret = PrintNumbers(No)

	print("Numbers till",No,":-")
	print(Ret)

def PrintNumbers(No) :

	Numbers = list()

	for i in range (1,No+1,1) :
		Numbers.append(i)

	return Numbers

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a number :-
12
Numbers till 12 :-
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

'''