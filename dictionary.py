print("Dictonary in python :\n")

student_details={"name":"Akshay","Roll-no":15,"City":"Ichalkaranji"}
print(type(student_details),student_details)
student_details["City"]="pune"
print(student_details)
print(student_details.keys())
print(student_details.values())
print(student_details.pop("City"))