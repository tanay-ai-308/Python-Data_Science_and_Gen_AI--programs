def main() :

	print("Enter Number :- ")
	No = int(input())

	Result = Factorial(No)

	print("Factorial of",No,"is :- ",Result)

def Factorial(No) :

	Sum = 1

	for i in range(1,No+1,1) :
		Sum = Sum*i

	return Sum

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter Number :-
6
Factorial of 6 is :-  720

'''