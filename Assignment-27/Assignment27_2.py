class BankAccount :

	ROI = 10.5

	def __init__(self,Name,Amount) :
		self.AccountHolder = Name
		self.Amount = Amount

	def Display(self) :
		print(f"Account Holder Name = {self.AccountHolder}\nTotal Balance = {self.Amount}")

	def Deposit(self,Amount) :
		self.Amount += Amount

	def Withdraw(self,Amount) :
		
		if (self.Amount>=Amount) :
			self.Amount -= Amount

	def CalculateInterest(self):
		Interest = (self.Amount*BankAccount.ROI)/100
		print(f"Interest on the {self.Amount} is {Interest}.")

Obj = BankAccount("Tanay",1500)
Obj.Display()

Obj.Deposit(2500)
Obj.Display()

Obj.Withdraw(1000)
Obj.Display()

Obj.CalculateInterest()