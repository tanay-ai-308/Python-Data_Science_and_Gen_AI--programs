class Circle :
	Pi = 3.14

	def __init__(self) :
		self.Radius = 0.0
		self.Area = 0.0
		self.Circumference = 0.0

	def Accept(self) :
		print("Enter the Radius :- ")
		self.Radius = float(input())

	def CalculateArea(self) :
		self.Area = (Circle.Pi) * (self.Radius**2)

	def CalculateCircumference(self) :
		self.Circumference = 2 * (Circle.Pi) * (self.Radius)

	def Display(self) :
		print("Radius = ",self.Radius)
		print("Area = ",self.Area)
		print("Circumference = ",self.Circumference)

def main() :

	Shape = Circle()

	Shape.Accept()
	Shape.CalculateArea()
	Shape.CalculateCircumference()
	Shape.Display()

if __name__ == "__main__" :
	main()