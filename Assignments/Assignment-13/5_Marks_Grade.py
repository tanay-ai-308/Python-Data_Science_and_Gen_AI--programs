def main() :

	print("=-"*22)
	print(" "*13,"Marks Grade")
	print("=-"*22)
	print("Enter the Number :- ")
	Num = int(input())

	Result = Grade(Num)

	print("Student got",Result)

def Grade(num) :

	if (num>=75) :
		return "Distinction."
	elif (num<75 and num>=60):
		return "First Class."
	elif (num<60 and num>=50):
		return "Second Class."
	else :
		return "Fail."

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
              Marks Grade
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Enter the Number :-
75
Student got Distinction.

'''