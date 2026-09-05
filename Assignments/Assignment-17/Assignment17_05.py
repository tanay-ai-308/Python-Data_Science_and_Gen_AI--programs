def main ():

	print("Enter a number :- ")
	No = int(input())

	Ret = CheckPrime(No)

	if (Ret) :
		print(No,"is a prime number.")
	else :
		print(No,"is not a prime number.")

def CheckPrime(No) :

	if (No<=1) :
		return 0
	else :
		for i in range (2,No,1) :
			if (No%i == 0) :
				return 0

		return 1

if __name__ == "__main__" :
	main ()