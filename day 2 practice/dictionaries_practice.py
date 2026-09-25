###-------------- dictionaries --------------

student={
"name":"haseeb",
"roll_no":"066",
"age":"21"
}
#1
print(student["name"])
#2
student.update({"name":"ahmed"})
print(student)
#3
student["phone"]="555-555"
print(student)
#4
del student["name"]
print(student)
#5
print(student.keys())
#6
print(student.values())
