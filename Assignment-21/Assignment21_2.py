import threading

def main() :

	NumList = list()

	print("How many number you want to enter :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		NumList.append(int(input(f"Number {i} = ")))

	Tobj1 = threading.Thread(target = Maximum, args = (NumList,))
	Tobj2 = threading.Thread(target = Minimum, args = (NumList,))

	Tobj1.start()
	Tobj2.start()

	Tobj1.join()
	Tobj2.join()

def Maximum(Numbers) :

	Max = Numbers[0]

	for No in Numbers :
		if(Max<No) :
			Max = No

	print(f"Maximum Number form list = {Max}")
	
def Minimum(Numbers) :

	Min = Numbers[0]

	for No in Numbers :
		if(Min>No) :
			Min = No

	print(f"Minimum Number form list = {Min}")

if __name__ == "__main__" :
	main()