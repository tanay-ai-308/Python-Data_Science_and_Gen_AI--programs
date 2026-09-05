def main() :

	print("Enter Number :- ")
	No = int(input())

	Result = EvenNumber(No)

	print("Even Numbers till",No,"are :- ")
	print(Result)

def EvenNumber(No) :

	Even = list()

	for i in range(1,No+1,1) :
		if(i%2 == 0) :
			Even.append(i)

	return Even

if __name__ == "__main__" :
	main ()