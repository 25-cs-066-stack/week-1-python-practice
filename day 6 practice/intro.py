"""import my_module
courses= ["history","math","physics","comp sci"]
index= my_module.find_index(courses,"comp sci")
print(index)


#------------------------------------------------------------------------------------------------------
#specifying module name (that we are importing)
import my_module as mm
courses =["history","math","physics","comp sci"]
index= mm.find_index(courses,"math")
print(index)


#-------------------------------------------------------------------------------------------------------
# using from for importing specific functionality from other module  (function/class)
from my_module import find_index
courses=["history","math","physics","comp sci"]
index=find_index(courses,"history")
print(index)

from my_module import find_index,test
courses= ["history","math","physics","comp sci"]
index =my_module.find_index(courses, "math")
print(index)
print(test)

          
#---------------------------------------------------------------------------------------------------
#  checking locations by system to find files in other modules
from my_module import find_index,test
import sys
courses =["history","mathj","physics","comp sci"]
index=my_module.find_index(courses,"math")
print(sys.path)
"""


# commmented out all above prcatice programs to run last program 


#----------------------------------------------------------------------------------------------------
# if modules are in different files/dirctories---
import sys
sys.path.append(r"C:\Users\haseeb ahmed\Desktop\my modules")
from my_module import find_index,test
courses =["math","physics","arts","bio"]
index=find_index(courses,"arts")
print(index)


#------------------------------------------------------------------------------------------------------------------
#after making variable changes  we can impot standard libraries of python (that are already written in python)
# using random library.

import random
courses=["history","math","physics","comp sci"]

random_courses= random.choice(courses)
print(random_courses)




#------------------------------------------------------------------------------------------------------------------------------

#standard library for perfoming  MATHMATICAL operations
import math
rad=math.radians(90)   #converting  90 degrees into radians.
print(rad)

#using standard librariares of math for finding sin value

import math
rad=math.radians(90)
print(math.sin(90))



#-------------------------------------------------------------------------------------------------------------------------------
# standard libraries for working datetime and calender
import datetime
import calendar

today=datetime.date.today()
print(today)

#using  calender library for cheking leap year 
leap_year=calendar .isleap (2020)
print(leap_year)


#-------------------------------------------------------------------------------------------------------------------------------
#standard library for OS module 
# os module aloow us to acess underlying module
import os
print(os.getcwd())  #cwd current file directory/file

#-------------------------------------------------------------------------------------------------------------------------------
#for location of file system 
import os
print(os.__file__)

####----------------------------------------------------------------------------------------------------------------------------

