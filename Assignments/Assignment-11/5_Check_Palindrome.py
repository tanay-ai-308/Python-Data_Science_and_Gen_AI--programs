def main ():

	print("Enter a number :- ")
	No = int(input())

	Ret = CheckPalindrome(No)

	if (Ret) :
		print("Number is Palindrome.")
	else :
		print("Number is not Palindrome.")
	
def CheckPalindrome(No) :

	Num = No
	RevNum = 0

	while (No > 0) :
		RevNum = (RevNum*10) + (No%10)
		No = int(No/10)

	if (RevNum == Num):
		return 1
	else :
		return 0

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a number :-
121
Number is Palindrome.

'''