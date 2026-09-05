def main() :

	print("Enter a number :- ")
	No = int(input())

	Ret = Factorial(No)

	print(Ret)

def Factorial(No) :

	Fact = 1

	for i in range (1,No+1,1) :
		Fact = Fact*i

	return Fact

if __name__ == "__main__" :
	main ()