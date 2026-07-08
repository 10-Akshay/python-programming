print("Inheritance in python :\n")
"""
class student:
    def __init__(self):
        self.name=input("Enter the name :")
        self.rollNo=int(input("Enter the roll no :"))
    def display_student(self):
        print("Name :",self.name)
        print("Roll no :",self.rollNo)
class test(student):
    def test_getdata(self):
        subject1=int(input("Enter the marks of subject 1 :"))
        subject2=int(input("Enter the marks of subject 2 :"))
        subject3=int(input("Enter the marks of subject 3 :"))
        subject4=int(input("Enter the marks of subject 4 :"))
        self.percentage=(subject1+subject2+subject3+subject4)/4
    def test_display(self):
        print("Total percentage :",self.percentage)
t=test()
t.test_getdata()
t.test_display()
t.display_student()

"""

class student:
    def __init__(self):
        self.name=input("Enter the name :")
        self.rollno=int(input("Enter the rollno :"))
    def display_student(self):
        print("Name :",self.name)
        print("Roll no :",self.rollno)
class test(student):
    def test_getdata(self):
        self.subject1=int(input("Enter the marks of subject 1 :"))
        self.subject2=int(input("Enter the marks of subject 2 :"))
        self.subject3=int(input("Enter the marks of subject 3 :"))
        self.subject4=int(input("Enter the marks of subject 4 :"))
        self.percentage=(self.subject1+self.subject2+self.subject3+self.subject4)/4
    def display_test(self):
        print("Total percentage :",self.percentage)
        if self.percentage>=90:
            print("Your the legend ")
        elif self.percentage>=70:
            print("You got first class ")
        elif self.percentage>=50:
            print("You are pass ")
        elif self.percentage>=35:
            print("You are pass only")
        else:
            print("You are fail, try next time")
class sports(test):
    def sports_getdata(self):
        print("Sports data :\n")
        self.weight=int(input("Enter your weight of sports :"))
        self.height=int(input("Enter your height of sports :"))
    def sports_displayData(self):
        print(self.weight)    
        print(self.height)    

s=sports()
s.display_student()
s.test_getdata()
s.display_test()
s.sports_getdata()
s.sports_displayData()
