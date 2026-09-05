def main ():

	print("Enter a number :- ")
	No = int(input())

	Ret = ReverseNumber(No)

	print("Revers of the number is :- ",Ret)
	
def ReverseNumber(No) :

	Num = 0

	while (No > 0) :
		Num = (Num*10) + (No%10)
		No = int(No/10)

	return Num

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a number :-
123
Revers of the number is :-  321

'''