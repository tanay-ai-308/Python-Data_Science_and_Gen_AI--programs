def main() :
	
	print("Enter number : ")
	No = int(input())

	Ret = Divisible3And5(No)

	if (Ret == 1) :
		print(No,"is divisible by both 3 and 5.")
	else :
		print(No,"is divisible by ",Ret)

def Divisible3And5(No) :
	
	if ((No%3==0) and (No%5==0)) :
		return 1
	elif (No%3 == 0) :
		return 3
	elif (No%5 == 0) :
		return 5
	else :
		return None

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-

Enter number :
15
15 is divisible by both 3 and 5.

'''