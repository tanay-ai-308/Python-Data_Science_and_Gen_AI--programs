def main() :

	print("Enter Number :- ")
	No = int(input())

	Result = SumOfNumber(No)

	print("Sum of first",No,"Natural number is :- ",Result)

def SumOfNumber(No) :

	Sum = 0

	for i in range(1,No+1,1) :
		Sum = Sum+i

	return Sum

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter Number :-
5
Sum of first 5 Natural number is :- 15

'''