def main() :

	print("Enter Number :- ")
	No = int(input())

	Result = OddNumber(No)

	print("Odd Numbers till",No,"are :- ")
	print(Result)

def OddNumber(No) :

	Odd = list()

	for i in range(1,No+1,1) :
		if(i%2 != 0) :
			Odd.append(i)

	return Odd

if __name__ == "__main__" :
	main ()

'''
OUTPUT :-
Enter Number :-
30
Odd Numbers till 30 are :-
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

'''