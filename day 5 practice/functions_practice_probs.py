# 1...Function that prints your name.
def name():
    print("haseeb ahmed")
name()    

# 2...Function that prints your university.

def uni_name():
    print("hitec university")
uni_name()

# 3.Function that prints your dream job

def dream_job():
    print("cloud security Architect, VCISO , CEO")
dream_job()

###-----------------------------------------------------------------------

# .Call each function multiple times...
name()
name()
name()

uni_name()
uni_name()
uni_name()

dream_job()
dream_job()
dream_job()


##-----------------------------------------------------------------


#Part 2 – Functions with Parameters
#Practice:
#Create functions that accept values like:
#Name
#Age
#University
#Semester
#CGPA
#Call them with different values.

def student_details(name,age,university,semester,CGPA):
 print("name:",name)
 print("Age:",age)
 print("university:",university)
 print("semester:",semester)
 print("CGPA:",CGPA)

student_details("haseeb",22,"hitec university",2,3.6)
student_details("ahmed",20,"hitec university",2,3.5)
student_details("Ali",21,"hitec university",2,3.4)



###-------------------------------------------------------------------

#Part 3 – Functions with Return
#Practice:
#Create functions that return:
#Sum of two numbers.
#Square of a number
##Cube of a number.

def sum(a,b):
   return(a+b)
result=sum(2,3)
print(result)


def square(num):
   return(num*num)
result=square(5)
print(result)


def cube(num):
   return(num*num*num)
result=cube(5)
print(result)

##----------------------------------------------------------------

#☁️ Part 4 – Cloud Practice

#Create a function named conceptually like check_server_status.
#It should accept:
#Server name
#Server status (True or False)
#Then display whether the server is running or stopped.

def check_server_status(name,server_status):
  if server_status:
     print(name,"is runnig")
  else:
     print(name,"is stopped")
check_server_status("web 01",True)
check_server_status("web 02",False)
check_server_status("web 03",True)


###---------------------------------------------------------------------


def cpu_checker(name,usage):
 if usage >= 80:
    print(name,"high cpu usage")
 else:
    print(name,"cpu is Healthy")
cpu_checker("cpu 01 : ",60)
cpu_checker("cpu 02 : ",87)
cpu_checker("cpu 03 : ",45)


###--------------------------------------------------------------
#🏆 Mini Challenge
#Create a simple "Cloud Report".
#Store:
#5 server names
#Their CPU usage values
#Use a loop to call your function for each server.
#This combines:

#Functions
#Loops
#Lists
#if statements

def check_cpu(server_name,usage):
   if usage < 80:
      print(server_name ,":",usage," % - Cpu is normal ")
   else:
      print(server_name,":",usage,"%_ cpu is not normal ")
servers = ["web-01","web_02","database-01","app-01","back-01"]
cpu_usage = [34,90,67,86,87]

for i in range(len(servers)):
   check_cpu(servers[i],cpu_usage[i])

   