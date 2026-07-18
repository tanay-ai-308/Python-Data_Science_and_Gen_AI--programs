class Arithmatic :

    def __init__ (self) :
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self) :
        print("Enter 1st number : ")
        self.Value1 = int(input())

        print("Enter 2nd number : ")
        self.Value2 = int(input())

    def Addition(self) :
        Ans = self.Value1+self.Value2
        return Ans

    def Subtraction(self) :
        Ans = self.Value1-self.Value2
        return Ans

    def Multiplication(self) :
        Ans = self.Value1*self.Value2
        return Ans

    def Division(self) :
        Ans = self.Value1/self.Value2
        return Ans
    
AObj = Arithmatic()

print("For Addition enter 2 numbers :- ")
AObj.Accept()
Ret = AObj.Addition()          #Ret = Addition(AObj,Value1,Value2)
print("Addition is : ",Ret)

print("For Subtraction enter 2 numbers :- ")
AObj.Accept()
Ret = AObj.Subtraction()
print("Subtraction is : ",Ret)

print("For Multiplication enter 2 numbers :- ")
AObj.Accept()
Ret = AObj.Multiplication()
print("Multiplication is : ",Ret)

print("For Division enter 2 numbers :- ")
AObj.Accept()
Ret = AObj.Division()
print("Division is : ",Ret)