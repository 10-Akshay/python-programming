print("*** Student details ***")
name=input("Enter the name : ")
rollno=int(input("Enter the roll no :"))
print("Name :", name)
print("Roll no :", rollno)
subject1=int(input("Enter the marks of english :"))
subject2=int(input("Enter the marks of maths :"))
subject3=int(input("Enter the marks of science :"))
subject4=int(input("Enter the marks of social :"))
percentage=(subject1+subject2+subject3+subject4)/4
print("Percentage :",percentage)
if percentage>=90:
    print("You get grade A")
elif percentage>=70:
    print("You get grade B")
elif percentage>=50:
    print("You get grade C")
elif percentage>=35:
    print("Your pass only")
else:
    print("Your fail")
