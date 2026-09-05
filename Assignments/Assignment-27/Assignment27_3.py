class Numbers :

	def __init__(self,No) :
		self.Value = No

	def ChkPrime(self) :
		if (self.Value<=1) :
			return False
		else :
			for i in range (2,self.Value,1) :
				if (self.Value%i == 0) :
					return False
			return True

	def SumFactors(self) :
		Sum = 0

		for i in range(1,self.Value+1,1) :
			Sum = Sum + i

		print("Sum of all factors is = ",Sum)

	def Factors(self) :
		Fact = list()
		print(f"Factors of {self.Value} are :-")
		for i in range(1,self.Value+1,1) :
			Fact.append(i)

		print(Fact)

	def ChkPerfect(self) :

		num = self.Value 
		Sum = 0

		while(num) :
			Sum = Sum + (num//10)
			num = num//10

		if (self.Value == Sum) :
			return True
		else :
			return False

Obj = Numbers(11)

Obj.Factors()
Obj.SumFactors()
print(Obj.ChkPrime())
print(Obj.ChkPerfect())