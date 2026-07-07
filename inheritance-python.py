print("Inheritance in python :\n")

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

