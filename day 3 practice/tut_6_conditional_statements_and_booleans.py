#conditionals and boolean.

# COMPARISONS
# 1.equal==
# 2.not equal !=
# 3.greater than >
# 4.less than <
# 5.greater then or equal to >=
# 6.less then or equal to <=
# object identity  : is 


 #           if, else , elif



 # == operator
if language == "python":
    print("language is python")
else:
    print("no match")

#---------------------------------------------------------------------------------------------------------------

#checking multiple language/items/strings using elif ...

language="java script"
if language == "python":
    print("language is python")
elif language== "java script":
    print("language is java script")
else:
    print("no match")

#-----------------------------------------------------------------------------------------------------------------

# boolean operator
# and 
# or 
# not



# using and boolean operator  (for true both condition must satisfy in and operator )
   
user= "admin"
logged_in= False # the  false that is used in that is built in 
if user =="admin" and logged_in:
   print ("Admin page")
else:
    print("log in first")


user= "admin"
logged_in= True # the  True that is used in that is built in 
if user =="admin" and logged_in:
    print ("Admin page")
else:
    print("log in first")

#-----------------------------------------------------------------------------------

 #          or operator   ( for this any one of condtiton must be true )
 
user="admin" 
logged_in= False
if user== "admin"or logged_in: # login in is false but output will be  admin page because of or condition 
    print("admin page")
else:
    ("please log in first ")



#-------------------------------------------------------------------------------------

# NOT OPERATOR

user="admin"
logged_in=False  # output is login first because of logged_in variable is False 

if not logged_in:
    print("log in first")
else:
    print("admin page")



#  with logged_in =True

user="admin"
logged_in=True  # output is admin page because of the varbile looged_in is True by default 
if not logged_in:
   print("log in first")
else:
   print("admin page")


# -------------------- FALSE VALUES ------------------------------------
# false
# none
# zero of any numeric type.
# any empty sequences ... e.g " ",( ),[].
# any empty mapping... e.g {}


# False  ( condtiton is  SET TO BE false)
condition = False
if condition:
   print("evaluated to true")
else:
    print("evaluted to false")

# None 
condition = None   # out put is none because its set to be none 
if condition:
    print("evaluated to true")
else:
    print("evaluted to false")


# for zero /  numeric conditions 

condition = 0  # output is false because its set to be 0 
if condition:
    print("evaluated to true")
else:
    print("evaluted to false")

#condition = 10   # out put is true because its set to be numeric value 
if condition:
    print("evaluated to true")
else:
    print("evaluted to false")

#---------------------------------------------------------------------------------------


#empty sequence [] , " "
condition=[]
if condition:
    print("evalute to true")
else:
    print("evaluted to false") 


#---------------------------------------------------------------------------

# empty mapping {}

condition={}
if condition:
    print("evalute to true")
else:
    print("evaluted to false") 






