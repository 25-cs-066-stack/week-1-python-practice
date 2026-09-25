#     loops and Iterations - For/While Loops

# for loop

nums= [1,2,3,4,5]
for num in nums:
    print(num)



# for loop with break   (use to stop loop after finding specific value or condition )

Nums = [1,2,3,4,5]
for num in Nums:
    if num==3:
        print("found it !")
        break
    print(num)


# for loop with continue  ( use to continue loop after meeting the given condition  )
  
numbs = [1,2,3,4,5]
for num in numbs:
    if num==4:
        print("fount it !")
        continue
    print(num)

# for loop (nested)

test_nums = [1,2,3,4,5,6]
for num in test_nums:
    for letters in "abc":
        print(num,letters)


# loop using range  (we use range to print some thing for specific times).
# basically it starts from 0 .

for i in range (10):
    print(i)

# loop using range but (start printing from 1) .
# using 11 because by default it skips last value
for i in range (1,11): 
    print(i)




# ------------------------------WHILE LOOP ---------------------------------------
# While loop is used to print something for specific times 
x = 0

while x < 10: 
  print(x)
  x=x+1


# while loop with (break function)

x = 0

while x < 10:
    if x== 5:
        print ("its 5")
        break
    print(x)
    x+=1


#  while loop (empty loop)   to stop that we press ctrl + c

x = 0

#while True:
#    print(x)
#    x+=1
    