class Demo :

	Value = None

	def __init__(self, Param1, Param2) :
		self.No1 = Param1
		self.No2 = Param2

	def Fun(self):
		print("No1 = ",self.No1)
		print("No2 = ",self.No2)

	def Gun(self):
		print("No1 = ",self.No1)
		print("No2 = ",self.No2)

def main():

	Obj1 = Demo(11,21)
	Obj2 = Demo(51,101)

	Obj1.Fun()
	Obj2.Fun()

	Obj1.Gun()
	Obj2.Gun()

if __name__ == "__main__" :
	main()