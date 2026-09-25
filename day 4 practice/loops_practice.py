# ------------------ BASIC LOOPS --------------------
#    for loop


# 1- Print your name 10 times.

for i in range(10):
     print( "HASEEB AHMED")

# 2- Print numbers from 1 to 10.
  
num = [1,2,3,4,5,6,7,8,9,10]
for num in num:
     print(num)

#  3-Print numbers from 10 to 1.
numbers=[10,9,8,7,6,5,4,3,2,1]
for num in numbers:
     print(num)



# 4- Print even numbers from 1 to 20.
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in nums:
     if num%2==0:
         print(num)

# 5-print odd numbers from 1 to 20.
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in numbers:
    if num%2!=0:
        print(num)


# PART 2 lists + loops 
fruits=["mango","apple","banana"]
for fruit in fruits:
    print(fruit)

programming_languages = ["bash","java script","python"]
for programming_language in programming_languages:
    print(programming_language)

cloud_platforms=["aws","gcp","azure"]
for cloud_platform in programming_languages:
   print(cloud_platform)   


for fruit,programming_language,cloud_platform in fruits,programming_languages,cloud_platforms:
    print(fruit,programming_language,cloud_platform)


# Part 3 – break
#Practice:
#Print numbers from 1 to 10.
#Stop when the number reaches 5.


nums= [1,2,3,4,5,6,7,8,9,10]
for num in nums:
    if num==5:
        print("found it ! its no 05")
        break
    print(num)



#Part 4 – continue
#Practice:
#Print numbers from 1 to 10.
#Skip the number 5.

number= [1,2,3,4,5,6,7,8,9,10]
for num in number:
 if num==5:
    print("skipped that value of 5")
    continue
 print(num)   





# Part 5 – while Loop
# Practice:
# Print numbers from 1 to 5.
# Print your name 5 times

x=1
while x<=5:
   print(x)
   x+=1


count = 1
while count <= 5:
   print("haseeb") 
   count+=1



   