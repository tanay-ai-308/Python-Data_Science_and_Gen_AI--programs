def main ():

	print("Enter a number :- ")
	No = int(input())

	Ret = SumDigit(No)

	print("Sum of the number is :- ",Ret)
	
def SumDigit(No) :

	Sum = 0

	while (No > 0) :
		Sum = Sum + (No%10)
		No = int(No/10)

	return Sum

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a number :-
123
Sum of the number is :-  6

'''