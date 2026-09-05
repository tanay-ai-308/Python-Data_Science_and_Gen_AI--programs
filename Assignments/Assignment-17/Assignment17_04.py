def main() :

	print("Enter a number :- ")
	No = int(input())

	Ret = SumOfFactors(No)

	print(Ret)

def SumOfFactors(No) :

	Factors = 0

	for i in range (1,No,1) :
		if (No%i == 0) :
			Factors = Factors+i

	return Factors

if __name__ == "__main__" :
	main ()