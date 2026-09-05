def main():
    print("Enter 1st number = ")
    no1 = int(input())

    print("Enter 2nd number = ")
    no2 = int(input())

    Sum = Addition(no1 , no2)
    print("Addition is = ",Sum)

    Dif = Subtraction(no1 , no2)
    print("Subtraction is = ",Dif)

    Mult = Multiplication(no1 , no2)
    print("Multiplication is = ",Mult)

    Div = Division(no1 , no2)
    print("Division is = ",Div)

def Addition(No1 , No2):
    return No1 + No2
     
def Subtraction(No1 , No2):
    return No1 + No2

def Multiplication(No1 , No2):
    return No1 * No2

def Division(No1 , No2):
    return No1 / No2

if __name__ == "__main__" :
    main()

'''
OUTPUT :-

Enter 1st number =
12
Enter 2nd number =
12
Addition is =  24
Subtraction is =  24
Multiplication is =  144
Division is =  1.0

'''