def main() :

	print("Enter a Number :- ")
	No = int(input())

	Ret = Square(No)

	print(f"{No} power of two = {Ret}")

Square = lambda No1 : No1**2

if __name__ == '__main__':
	main()