# for getting current working directory
import os
current_directory = os.getcwd()
print(current_directory)


#------------------------------------------------------------------------

# for getting files and folder list in the directory
import os
lists = os.listdir()
print(lists)


#--------------------------------------------------------------------------
# for checking existence3 of file/folder 
import os
check_existence = os.path.exists("os_module-practice.py")
print(check_existence)

#--------------------------------------------------------------------------
# for checking file 
import os
file_check = os.path.isfile("OS-MODULE.py")
print(file_check)



#---------------------------------------------------------------------------
#for checking dirctory ....
import os
check_directory = os.path.isdir(os.getcwd())
print(check_directory)



#------------------------------------------------------------------------------
#for joining folder and file  to complete path we use os.path.join("folder","any text.file")
import os
"file.txt"
joining_path = os.path.join("os_module-practice.py","-","file.txt")
print(joining_path)

