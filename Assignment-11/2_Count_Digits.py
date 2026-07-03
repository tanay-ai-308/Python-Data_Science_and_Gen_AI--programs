def main ():

	print("Enter a number :- ")
	No = int(input())

	Ret = CountDigit(No)

	print(No,"is a has",Ret,"digits.")
	
def CountDigit(No) :

	Count = 0

	if(No == 0) :
		Count = Count+1
	else :
		while (No > 0) :
			Count = Count+1
			No = int(No/10)

	return Count

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a number :-
12345
12345 is a has 5 digits.

'''