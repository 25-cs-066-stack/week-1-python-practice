# Whether a student gets a scholarship
grade= "A"
github_portofolio = True
if grade=="A" and github_portofolio:
    print("congratulations : full scholar ship")
elif grade=="B" and github_portofolio:
    print(" 70%  Scholarship")
elif grade=="B" or github_portofolio:
    print( "30%  Scholarship ")
else:
    print("no Scholar ship ")



# Whether a person can vote.

age = 16
id= False
if age >= 18 and id:
    print("you are eligible to vote")
elif age >= 18:
    print("bring your id")
else:
    print("you are under age ")   


    

#Whether someone is eligible for admission


marks = 85
age = 18
entry_test_passed = True
documents_submitted = True

if    age >= 17 and marks >= 60 and entry_test_passed and documents_submitted:
    print("conratulations you got admission")
elif  age < 17 and marks >= 60 and entry_test_passed and documents_submitted:
    print ("you are under age")
elif  age >= 17 and marks < 60 and entry_test_passed and documents_submitted:    
    print ("marks less then 60 are not required")
elif age >= 17 and marks >= 60 and documents_submitted:
    print ("pass the entery test first ")
elif age >= 17 and marks >= 60 and entry_test_passed:
    print("submitt the document first")
else: 
    print(" full fill all the requiremnts for admisson ")





# cloud server
server_name = "black box"
cpu_usage = 65
memory_usage = 60
disk_usage = 70
server_running= True

print("server_name")

if cpu_usage <= 80 and memory_usage <= 80 and disk_usage <=80 and server_running:
 print("server is healthy")
elif cpu_usage > 80 and memory_usage <= 80 and disk_usage <=80 and server_running:
 print("warning !  high cpu usage")
elif cpu_usage <= 80 and memory_usage > 80 and disk_usage <=80 and server_running: 
 print(" warning ! high memory usage")
elif cpu_usage <= 80 and memory_usage <= 80 and disk_usage >80 and server_running:
   print("warning ! disk usage is high")
elif cpu_usage <= 80 and memory_usage <= 80 and disk_usage <=80:
   print("server is not running ")
else:
   print("check out there is error") 









     

     

  
