import os
cloud_system_directory = "cloud_system"
logs_directory = "logs"

logs_directory=os.path.join(cloud_system_directory,logs_directory)

os.makedirs(cloud_system_directory,exist_ok=True)
os.makedirs(logs_directory,exist_ok=True)


if os.path.isdir(cloud_system_directory):
    print("cloud system directory exists")
else:
    print("coud system directory dos not exists")

if os.path.isdir(logs_directory):
    print("logs directory exists")
else:
    print("log directory does not exists")


        
