import threading

def main() :

	print("Enter the number :- ")
	No = int(input())

	Tobj1 = threading.Thread(target = EvenFactor,args = (No,))
	Tobj2 = threading.Thread(target = OddFactor,args = (No,))

	Tobj1.start()
	Tobj2.start()

	Tobj1.join()
	Tobj2.join()

	print("Exit from main...")

def EvenFactor(No) :

	Sum = 0

	for i in range(1,No+1,1):
		if(No%i == 0 and i%2 == 0) :
			Sum = Sum+i

	print(f"Sum of all even Factors of {No} = {Sum}")

def OddFactor(No) :

	Sum = 0

	for i in range(1,No+1,1):
		if(No%i == 0 and i%2 == 1) :
			Sum = Sum+i

	print(f"Sum of all Odd Factors of {No} = {Sum}")

if __name__ == "__main__" :
	main ()