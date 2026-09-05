def main() :

	print("=-"*30)
	print(" "*13,"For the Area of Rectangle give")
	print("=-"*30)
	print("Enter the length :- ")
	Length = int(input())

	print("Enter the width :- ")
	Width = int(input())

	Area = RectangleArea(Length,Width)

	print("Area of Rectangle = ",Area)

def RectangleArea(length,width) :
	return (length * width)

if __name__ == "__main__" :
	main()


'''
OUTPUT :-

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
              For the Area of Rectangle give
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Enter the length :-
12
Enter the width :-
6
Area of Rectangle =  72

'''