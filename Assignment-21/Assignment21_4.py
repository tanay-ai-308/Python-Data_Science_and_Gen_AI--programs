import threading

def main() :

	NumList = list()
	Result = {"Add": 0 ,"Multi": 0}
	print("How many number you want to enter :- ")
	No = int(input())

	for i in range(1,No+1,1) :
		NumList.append(int(input(f"Number {i} = ")))

	Tobj1 = threading.Thread(target = Sum, args = (NumList,Result))
	Tobj2 = threading.Thread(target = Product, args = (NumList,Result))

	Tobj1.start()
	Tobj2.start()

	Tobj1.join()
	Tobj2.join()

	print(f"Sum of all Numbers = {Result["Add"]}")
	print(f"Product of all Numbers = {Result["Multi"]}")

def Sum(Numbers,Result) :

	Total = 0

	for No in Numbers :
		Total = Total+No

	Result["Add"] = Total

def Product(Numbers,Result) :

	Total = 1

	for No in Numbers :
		Total = Total*No

	Result["Multi"] = Total

if __name__ == '__main__':
	main()