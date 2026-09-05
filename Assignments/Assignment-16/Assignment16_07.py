def main() :

	print("Enter Number = ")
	No = int(input())

	Ret = ChkNum(No)

	print(Ret)
	
def ChkNum(No) :

	if(No%5 == 0):
		return True
	else :
		return False

if __name__ == "__main__" :
	main()