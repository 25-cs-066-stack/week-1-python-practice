#  empty function 
#def hello_function():

#    pass
#hello_function  # we use same function name with () to print function when we crreated print statement inside the function


#--------------------------------------------------------------------------------


#def hello_function():
#   pass  # pass is the key word that we use for running empty function 
#print(hello_function())  

#---------------------------------------------------------------------------------

# function with print value inside 
#def hello_function():
#   print(" this is hellooo function! ")

#hello_function()

#---------------------------------------------------------------------------------

# funtion with return 
#def hello_function():
#    return"hellooo function ! "  # the return will make the statement a string so we can  perform funtions on that string 

#print(hello_function())

#----------------------------------------------------------------------------------

# inside the function perfoming upper case function on the string 
#def hello_function():
#    return"this is first hello function"

#print(hello_function().upper())

#------------------------------------------------------------------------------------

#def hello_func(greeting): # greeting is parameter to functions
#    return"{}.function".format(greeting)

#print(hello_func("hiii")) # hiii is the argument 

#----------------------------------------------------------------------------

#def hello_func(greeting, name="you"):  # passing parameter as a argument
#     return"{},{}".format(greeting,name)

#print(hello_func("hi"))l..hh

#-----------------------------------------------------------------------------

def hello_function(greeting, name="you"):
    return"{},{}".format(greeting,name)

print(hello_function("hyyyy",name="haseeb"))
# In this example we have passed argument name with parameters
# In print line we also passed arguments name 
#------------ By default the program will print the name that we have passed i n print line........


#-------------------------------------------------------------------------------


# ----------------------------Positional keyword argument---------------------------

def student_info(*args,**kargs):  # In that we used * and ** with para meter to sort lists and dictionaries in the output  
    print(args)
    print(kargs)
student_info("math","comp sci",name="haseeb",age=22)
#  * and ** without these  in the output list and dictionaries will be in the same line  


#--------------------------------------------------------------------------------------------

coureses=["math","art"]
info={"name":"haseeb","age":22}
student_info (*coureses,**info) #   * and ** with using arguments it will also pritn the list and dictionaries seprately 







