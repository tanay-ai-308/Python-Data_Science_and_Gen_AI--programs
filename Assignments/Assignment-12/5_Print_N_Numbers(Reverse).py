def main() :

	print("Enter a number :- ")
	No = int(input())

	Ret = PrintNumbers(No)

	print("Numbers from",No,":-")
	print(Ret)

def PrintNumbers(No) :

	Numbers = list()

	for i in range (No,0,-1) :
		Numbers.append(i)

	return Numbers

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a number :-
10
Numbers from 10 :-
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

'''