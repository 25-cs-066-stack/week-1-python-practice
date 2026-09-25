import os
servers = "servers"
web_server_directories= os.path.join(servers,"web server")
database_server_directory =os.path.join(servers,"Database server")
backup_server_directory= os.path.join(servers,"back up server")

os.makedirs(web_server_directories,exist_ok=True)
os. makedirs(database_server_directory,exist_ok=True)
os.makedirs(backup_server_directory,exist_ok=True)

if os.path.isdir(web_server_directories):
    print("web server directory exists")
else:
    print("web server directory doesnot exists")

if os.path.isdir(database_server_directory):
    print("database server directory exists")
else:
    print("database directory doesnot exists")    

if os.path.isdir(backup_server_directory):
    print("backup server directory exists")
else:
    print("backup server directory doesnot exists")
    


