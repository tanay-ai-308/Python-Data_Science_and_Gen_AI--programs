def main() :
	
	Lst = list()
	print("How many number you want to enter : ")
	No = int(input())

	print(f"Enter {No} strings : ")
	for i in range(0,No,1):
		Lst.append((input()))

	FData = list (filter(Size,Lst))

	print("String greater than 5 are : ",FData)

Size = lambda String : String if (len(String)>5) else None

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

How many number you want to enter :
4
Enter 4 strings :
Indian
Bali
Japan
Usa
String greater than 5 are :  ['Indian']

'''