import threading

def main() :

	NumList = list()

	print("How many numbers you want to enter :- ")
	No = int(input())

	print(f"Enter {No} elements :- ")

	for i in range (1,No+1,1):
		NumList.append(int(input(f"{i} number = ")))

	Tobj1 = threading.Thread(target=EvenList, args=(NumList,))
	Tobj2 = threading.Thread(target=OddList, args=(NumList,))

	Tobj1.start()
	Tobj2.start()

	Tobj1.join()
	Tobj2.join()

def EvenList(Numbers) :

	Sum = 0

	for No in Numbers :
		if(not No%2) :
			Sum = Sum+No

	print("Sum of all even numbers from the list = ",Sum)

def OddList(Numbers) :

	Sum = 0

	for No in Numbers :
		if(No%2) :
			Sum = Sum+No

	print("Sum of all Odd numbers from the list = ",Sum)

if __name__ == '__main__':
	main()