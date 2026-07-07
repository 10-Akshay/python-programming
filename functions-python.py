def addition(no1,no2):
    print("Addition :",no1+no2)
def substraction(no1,no2):
    print("Substraction :",no1-no2)
def multiplication(no1,no2):
    print("Multiplication :",no1*no2)
def division(no1,no2):
    print("Division :",no1/no2)

print("Arithmatic operations")
no1=int(input("Enter the 1st no :"))
no2=int(input("Enter the 2nd no :"))
choice=int(input("Enter the choice :\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n"))
if choice==1:
    addition(no1,no2)
elif choice==2:
    substraction(no1,no2)
elif choice==3:
    multiplication(no1,no2)
elif choice==4:
    division(no1,no2)
else:
    print("Invalid choice")



