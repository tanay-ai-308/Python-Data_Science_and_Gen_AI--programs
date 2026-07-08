import Arithmetic

def main() :

	print("Enter 1st number :- ")
	No1 = int(input())

	print("Enter 2nd number :- ")
	No2 = int(input())

	Ret = Arithmetic.Add(No1,No2)
	print(f"{No1}+{No2}={Ret}")

	Ret = Arithmetic.Sub(No1,No2)
	print(f"{No1}-{No2}={Ret}")
	
	Ret = Arithmetic.Multi(No1,No2)
	print(f"{No1}*{No2}={Ret}")
	
	Ret = Arithmetic.Div(No1,No2)
	print(f"{No1}/{No2}={Ret}")

if __name__ == "__main__" :
	main ()