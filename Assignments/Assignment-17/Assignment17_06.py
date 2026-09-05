def main() :
	
	print("Enter Number = ")
	No = int(input())

	Display(No)

def Display(No) :

	for i in range(0,No,1) :
		print(" *"*(No-i))

if __name__ == "__main__" :
	main()