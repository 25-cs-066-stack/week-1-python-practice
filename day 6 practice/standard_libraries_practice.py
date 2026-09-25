import math
#1.math.sqrt()
square=math.sqrt(49)
print(square)

#------------------------------------------------

#ceil is used to round up (after decimal) the value to  up (round up)
import math     
ceil=math.ceil(5.4)
print(ceil)


#-------------------------------------------------
# math.floor is round down the value (by rounding off the value which is after decimal)

import math
floor=math.floor(4.6)
print(floor)

#----------------------------------------------------
# random library is used to print random values with randint
import random
value= random.randint(1,10)
print(value)

#-------------------------------------------------------------------------

# for chosing random thing from list random.choice library is used
import random
servers = ["web-01","web-03","web-09","web-04"]
value=random.choice(servers)
print(value)

#------------------------------------------------------------------------
# import os is basically used for (python + operating system)
import os
current_directory = os.getcwd()     # get here is for getting function and cwd is current working directory.(for checking which file of os is used b python currently)
print(current_directory)

#--------------------------------------------------------------------------------------------------------
# List files and folders.
# os.listdir()  this shows the current files/folders inside a current directory
import os
list=os.listdir()
print(list)

#---------------------------------------------------------------------------------------------------------
# os.path.exists("file/folder name to check") >>> check weather the file/folder exists
import os
check=os.path.exists("main.py") # path is a part of the os module that provides tools for working with file and folder paths.
print(check)

#---------------------------------------------------------------------------------------------------------
#  checking Environment variables...
import os 
check_environment= os.environ.get("path")
print(check_environment) 


