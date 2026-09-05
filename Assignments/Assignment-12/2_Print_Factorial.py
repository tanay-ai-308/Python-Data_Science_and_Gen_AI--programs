def main() :

	print("Enter a number :- ")
	No = int(input())

	Ret = GiveFactors(No)

	print("Factors of ",No,":-")
	print(Ret)

def GiveFactors(No) :

	Factors = list()

	for i in range (1,No+1,1) :
		if (No%i == 0) :
			Factors.append(i)

	return Factors

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter a number :-
12
Factors of  12 :-
[1, 2, 3, 4, 6, 12]

'''