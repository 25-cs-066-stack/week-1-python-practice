# Dictionaries in python is a collection that stores data in key values 
# example
# 
# key = the word
# value = the meaning of that word
# 

# Example of student dictionary
#student= {
#"name" : "ali",        here name is the key and ali is its value.
#"age" : 21,            here age is the key and 21 is its value.
#"city" : "Wah cantt"   here city is the key and wah cantt is its value.
#}

#print(student)



######-----------------------------------tutorial practice---------------------------------
student={"name ":" haseeb","age":22,"courses":["maths","data"]}
print(student)  #printing student

print(student["courses"]) # printing specific value using key of that value

print(student.get("section","not found")) # using get function to avoid  error  while printing value that is not in dictionary and not found is the message that is going to be displayed instead of error 

student ["phone"]= "5555-555"  # adding new key and value to list  student 

print(student)

student.update({"name":"haseeb ahmed","age":20000,"phone":"55566-56656"}) # for updating and adding multiple keys/values to dictionaries at a time

print(student)

del student["age"] #using del function to delete a specific value of a dictionary
print(student)

# ---------------------------------- 2nd method - (pop- mehtod) --------------------------
#age=student.pop("age")   use pop menthod to get deleted value back that is deleted from list
#print(age)

#print(len(student))        # lenght of dictionaries.
#print(len(student.keys))   # printing lenght of just keys in dictionaries.
#print(len(student.values)) # printing lenght of just values of dictionaries.  


for keys in student:  # using for loop just to print keys  of dictionary student
 print(keys)


for keys,values in student.items(): #  using for loop to print the keys and values dictionary 
 print(keys,values)


