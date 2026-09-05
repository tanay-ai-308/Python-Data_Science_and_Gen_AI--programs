def main() :
	
	print("Enter Number = ")
	No = int(input())

	Ret = SumOfNumber(No)

	print(f"{Ret}")

def SumOfNumber(No) :

	Sum = 0

	while(No>0) :
		Sum = Sum+(No%10)
		No = No//10

	return Sum

if __name__ == "__main__" :
	main()