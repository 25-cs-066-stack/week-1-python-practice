import os 
info= dir(os)
print(info)
# dir(os) this will show us all the functions/methods that we can perform on that module

#----------------------------------------------------------------------------------------------------
import os
cwd= os.getcwd()  # os.cwd() is used for printing current working directory.
print(cwd)

# os.chdir() for changing working directory
#os.chdir("c:\Users\haseeb ahmed\Desktop\python learning\week 1")
#cwd=os.getcwd()
#print(cwd)

#-----------------------------------------------------------------------------------------------------

# for checking files and folders in the directory
import os
list = os.listdir()
print(list)

#------------------------------------------------------------------------------------------------------
# making new file ?folder in the directory 
"""
import os
os.mkdir("os-demo") # for making file/ folder
os.rmdir("os-demo") # for removing file/folder
list =os.listdir()
print(list)

#-------------------------------------------------------------------------------------------------------

# for making file/folders and their sub files/folder in the directory
import os
os.makedirs("os-demo/sub-demo-2") # for making folder and sub folder/file 
os.removedirs("os-demo/sub-demo-2") # for removing folder and sub folder/file
file=os.listdir()
print(file)

#---------------------------------------------------------------------------------------------------------
# renaming files 
import os
os.mkdir("demo-file-1")
list= os.listdir()
print(list)

os.rename("demo-file-1","renamed-demo-file-1")  #renamed "demo-file-1 " into "renamed-demo-file"
list1 = os.listdir()
print(list1) 

"""
#-----------------------------------------------------------------------------------------------------------
# For printing information such as ( all the methods that bwe can  perform on that file ) 
import os
information = os.stat("OS-MODULE.py")
print(information)

# for performing specific operation on the file 
import os
size = os.stat("OS-MODULE.py").st_size
print(size)

#-------------------------------------------------------------------------------------------------------------
# for printing moditification time that is human readable we use datetime library
import os 
from datetime import datetime

mod_time= os.stat("OS-MODULE.py").st_mtime
print(datetime.fromtimestamp(mod_time))

#---------------------------------------------------------------------------------------------------------------
#  for printing directory tree 
import os
for dirpath,dirnames,filenames in os.walk(os.getcwd()):
    print("path :",dirpath )
    print("directory :",dirnames)
    print("files :",filenames)

    print()

#---------------------------------------------------------------------------------------------------------------
# for printing specific  environment variable.

import os
variable= os.environ.get("home") 

print(variable)

#----------------------------------------------------------------------------------------------------------------
# combinig HOME directory with file name (1st)
# creating file with home path 
import os
home = os.path.expanduser("~")
print(home)

"text.txt"
file_path=  os.path.join(home, "test.txt") 
print(file_path)


#-------------------------------------------------------------------------------------------------------------------- 

# for base name of any path 
import os
base_name = os.path.basename(r"c:\Users\haseeb ahmed\Desktop\python learning\week 1\day 7 practice")
print(base_name)

#--------------------------------------------------------------------------------------------------------------------
#for getting directory name
import os 
dirctory_name = os.path.dirname(r"c:\Users\haseeb ahmed\Desktop\python learning\week 1\day 7 practice")
print(dirctory_name)

#--------------------------------------------------------------------------------------------------------------------
# for printing both (base name and directory name)
import os
both_names= os.path.split(r"c:\Users\haseeb ahmed\Desktop\python learning\week 1\day 7 practice")
print(both_names)

#--------------------------------------------------------------------------------------------------------------------
#  for checking exsistence of path in file system
import os
check_existence = os.path.exists(r"c:\Users\haseeb ahmed\Desktop\python learning\week 1\day 7 practice")
print(check_existence)

#---------------------------------------------------------------------------------------------------------------------
# for checking existence of directory 
import os
check_directory = os.path.isdir(r"c:\Users\haseeb ahmed\Desktop\python learning\week 1\day 7 practice")
print(check_directory)
#---------------------------------------------------------------------------------------------------------------------

import os
file_check = os.path.isfile("OS-MODULE.py") # checking file existence is that exsists
print(file_check)

#---------------------------------------------------------------------------------------------------------------------
import os
split=os.path.splitext(r"c:\Users\haseeb ahmed\Desktop\python learning\week 1\day 7 practice")
print(split)

#----------------------------------------------------------------------------------------------------------------------
# for printing all the directories............
import os
directories = (dir(os.path))
print(directories)




