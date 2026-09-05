import threading

def main() :

	NumList = list()

	print("How many number you want to enter :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		NumList.append(int(input(f"Number {i} = ")))

	TPrime = threading.Thread(target = Prime, args = (NumList,))
	TNonPrime = threading.Thread(target = NonPrime, args = (NumList,))

	TPrime.start()
	TNonPrime.start()

	TPrime.join()
	TNonPrime.join()

def Prime(Numbers) :

	PrimeNumbers = list()

	for No in Numbers:
		if(CheckPrime(No)) :
			PrimeNumbers.append(No)

	print(f"Prime Numbers from the List = {PrimeNumbers}")

def CheckPrime(No) :
	if (No<=1) :
		return 0
	else :
		for i in range (2,No,1) :
			if (No%i == 0) :
				return 0
		return 1

def NonPrime(Numbers) :

	NonPrimeNumbers = list()

	for No in Numbers :
		if(CheckPrime(No) == 0):
			NonPrimeNumbers.append(No)

	print(f"Non-Prime Numbers from the List = {NonPrimeNumbers}")

if __name__ == "__main__" :
	main()