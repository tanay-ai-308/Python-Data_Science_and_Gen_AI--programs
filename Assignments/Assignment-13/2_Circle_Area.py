def main() :

	print("=-"*30)
	print(" "*13,"For the Area of Circle give")
	print("=-"*30)
	print("Enter the Radius :- ")
	Radius = int(input())

	Area = CircleArea(Radius)

	print("Area of Circle = ",Area)

def CircleArea(radius) :
	return (radius*radius*3.14)

if __name__ == "__main__" :
	main()


'''
OUTPUT :-

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
              For the Area of Circle give
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Enter the Radius :-
5
Area of Circle =  78.5

'''