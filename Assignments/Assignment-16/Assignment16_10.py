def main() :

	print("Enter a string :- ")
	String = input()

	Len = LengthString(String)

	print("Length of string is :- ",Len)

def LengthString(String) :
	return(len(String))

if __name__ == "__main__" :
	main ()