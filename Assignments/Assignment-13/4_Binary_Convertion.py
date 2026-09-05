def main() :

	print("=-"*30)
	print(" "*13,"Binary Convertion")
	print("=-"*30)
	print("Enter the Number :- ")
	Num = int(input())

	Binary = BinaryConvertion(Num)

	print("Binary of",Num,"=",Binary)

def BinaryConvertion(num) :

	binary = 0
	place = 1

	while(num) :
		no = num%2
		binary = binary+no*place
		place = place*10
		num = num//2

	return binary

if __name__ == "__main__" :
	main()

'''
OUTPUT:-

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
              Binary Convertion
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Enter the Number :-
10
Binary of 10 = 1010

'''