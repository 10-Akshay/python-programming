print("Class and Object concept in python :\n")

class student:
    def __init__(self):
        self.name=input("Enter the name of student :")
        self.age=int(input("Enter the age of student :"))
    def display(self):
        print("Name :",self.name)
        print("Age",self.age)
a=student()
b=student()
c=student()
a.display()
b.display()
c.display()
