import threading

def main() :

	Tobj1 = threading.Thread(target = PrintEven)
	Tobj2 = threading.Thread(target = PrintOdd)

	Tobj1.start()
	Tobj2.start()

	Tobj1.join()
	Tobj2.join()

def PrintEven() :

	No = 1
	EvenList = list()

	while(len(EvenList) != 10) :

		if(No%2 == 0) :
			EvenList.append(No)
		No+=1

	print(f"1st 10 Even Number :- {EvenList}")

def PrintOdd() :

	No = 1
	OddList = list()

	while(len(OddList) != 10) :

		if(No%2 == 1) :
			OddList.append(No)
		No+=1

	print(f"1st 10 Odd Number :- {OddList}")

if __name__ == '__main__':
	main()