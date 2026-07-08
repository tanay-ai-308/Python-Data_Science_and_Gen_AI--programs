def main() :

	print("Enter 1st Number = ")
	No1 = int(input())

	print("Enter 2nd Number = ")
	No2 = int(input())

	Add(No1, No2)

def Add(No1, No2) :

	print(f"{No1}+{No2}={No1+No2}")

if __name__ == "__main__" :
	main()