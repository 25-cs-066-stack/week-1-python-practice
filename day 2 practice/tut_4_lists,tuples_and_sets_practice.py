###                                LISTS

#lists : collections of items thAT cxan be changed []

courses =["history","maths","comp sci"]

print(courses)
print(len(courses))  # for lenght of courses.
print(courses[0])    # for specific  value of list use index.
print(courses[-1])   # for for printing last value of index.

# Modifiying list 
courses.append("art")  # use append method to add a item in list. 
print(courses)

courses.insert(0,"art") # use insert method to add a item on a specific location on a list : The 0 here is the index where i want to put the value
print(courses)

courses_2=["art", "education"]
courses.extend(courses_2)   # extend method use merge two lists.   
print(courses)

courses.remove("maths") # remove to remove item from list. 
print(courses)

#2nd method of removing items
courses.pop()   # by default it removes the last item 
print(courses)

popped = courses.pop() # to get the value that is removed by pop method
print(popped)

courses.reverse()
print(courses)

#### list sorting

courses.sort() #uses to sort the items in asecending order
print(courses)

num=[5,3,2,4,1] #list of nums
num.sort() # sort method used to sort it by default 
print(num)

courses.sort(reverse=True) # used to reverse items order in descending order
print(courses)

num.sort(reverse=True) # for reverse order like in decesnding order
print(num)

print(min(num)) # for printing minimum numers of list 
print(max(num)) # for printing maximum number of list
print(sum(num)) # for sum of aLL the numbers in list 

#searching index of specific item on list 
print(courses.index("comp sci"))

print("art" in courses)  #for checking specific item on course.

#using for loop to print items of list 
for items in courses:
  print(items)

#using  for loop to print index and items of the list 
for index,items in enumerate (courses): #in for loop we use enumurate for index/items
  print(index,items)

  for index,items in enumerate (courses, start=1): #in for loop if we want to print both index and items 
    print(index,items)


#printing lists into strings
courses_2=["math","history","comp sci","physics"]
courses_str="-".join(courses_2) #printing courses into string  by using join 
print(courses_str)


#coverting string back into list 
new_list=courses_str.split("-")
print(new_list)









##### ----------------------------------  tuples ---------------------------------------  

#  tuples: representd by ()  list of items that cannot be changed after creation 
tuple_1=("math","art","comp sci","data")
tuple_2=tuple_1

print(tuple_1)
print(tuple_2)
# We cannot add,remove,append,insert,expand items tuples 
# Can perform other functions likes functions performed on functions 







####------------------------------------------ SETS ------------------------------------####
#sets : sets can change oder by default every time of execution
# and can remove values by default 

cs_courses={"math","dsa","oop","dbms"}
print("dsa"in cs_courses)

#    With two sets
cs_courses1={"math","dsa","oop","dsa"}
art_courses={"math","history","dsa","data"}

#for printing same courses we use intersection 
print(cs_courses1.intersection(art_courses))

#for printing courses that are different in set 1  we use difference method 
print(cs_courses1.difference(art_courses))

#for printing courses in one set we use union method 
print(cs_courses.union(art_courses))





