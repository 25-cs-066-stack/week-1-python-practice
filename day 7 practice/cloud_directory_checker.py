import os

# creating server directory...

server_directory= "cloud_server"
os.makedirs(server_directory,exist_ok=True)

logs_directory = os.path.join("server_directory","logs")

# creating logs directory...

os.makedirs(logs_directory,exist_ok=True)


# creating configration file 
config_file = os.path.join(server_directory,"config.txt")

if os.path.exists(config_file):
    print("configration file exists")
else:
    print("confiration file  exists")


if os.path.exists(server_directory):
    print(" server directory exists ")
else:
    print("server directory does not exists")


if os.path.isdir(logs_directory):
    print("log directory exists")
else:
    print("log directory does not exists")
 
 
