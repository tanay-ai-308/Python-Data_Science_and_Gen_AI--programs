def main() :

	print("Enter Number = ")
	No = int(input())

	ChkNum(No)

def ChkNum(No) :

	if(No>0) :
		print("Positive Number.")
	elif(No<0) :
		print("Negative Number.")
	else :
		print("Zero.")
		
if __name__ == "__main__" :
	main()