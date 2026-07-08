def main() :

	print("Enter Number = ")
	No = int(input())

	ChkNum(No)

def ChkNum(No) :

	if(No%2 == 0):
		print("Even Number.")
	else :
		print("Odd Number.")

if __name__ == "__main__" :
	main()