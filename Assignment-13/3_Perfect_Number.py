def main() :

	print("=-"*22)
	print(" "*13,"Perfect Number")
	print("=-"*22)
	print("Enter the Number :- ")
	Num = int(input())

	Result = PerfectNumber(Num)

	if (Result) :
		print(Num,"is Perfect Number.")
	else :
		print(Num,"is not a Perfect Number.")

def PerfectNumber(num) :

	Org = num 
	Sum = 0

	while(num) :
		Sum = Sum + (num//10)
		num = num//10

	if (num == Sum) :
		return 1
	else :
		return 0

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
              Perfect Number
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Enter the Number :-
6
6 is Perfect Number.

'''