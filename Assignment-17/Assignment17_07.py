def main() :
	
	print("Enter Number = ")
	No = int(input())

	Display(No)

def Display(No) :

	for i in range(1,No+1,1) :
		for j in range(1,No+1,1) :
			print(j,end = "  ")
		print()
if __name__ == "__main__" :
	main()