import os
sevrer_backup="server_backup"  # creating variable
database_directory = "directory" # creating variable

database_directory= os.path.join(sevrer_backup,database_directory)  #making address by joining them

os.makedirs(sevrer_backup,exist_ok=True)
os.makedirs(database_directory,exist_ok=True)

if os.path.isdir(sevrer_backup):
    print("backup directory exists")
else:
    print("server back up doesnot exists")

if os.path.isdir(database_directory):
    print("data base directory exists")
else:
    print("data base directory doesnot exists")

