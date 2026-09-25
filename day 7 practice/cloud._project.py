import os
cloud_project= "cloud project"
logs_directory= os.path.join(cloud_project,"logs")
config_directory = os.path.join(cloud_project,"configration directory")
backup_directory = os.path.join(cloud_project,"back directory")

os.makedirs(cloud_project,exist_ok=True)
os.makedirs(logs_directory,exist_ok=True)
os.makedirs(config_directory,exist_ok=True)
os.makedirs(backup_directory,exist_ok=True)


if os.path.isdir(cloud_project):
    print("cloud project directory exists")
else:
    print("cloud project directory doesnot exists")

if os.path.isdir(logs_directory):
    print("logs directory exists")
else:
    print("logs directory doesnot exists")    

if os.path.isdir(config_directory):
    print("config directory exists")
else:
    print("config directory doesnot exists")

if os.path.isdir(backup_directory):
    print("backup directory exists")
else:
    print("backup directory doesnot exists")    
    