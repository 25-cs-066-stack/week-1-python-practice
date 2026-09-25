def server_check(name,cpu,memory,status):
    if not status:
        print(name,"server is off")
    elif cpu >=80:
        print(name,"warning !!! cpu usage is high ")    
    elif  memory >=80:
        print(name,"warning high memory usage ")
    else:
        print(name,"server is working perfectly")

    
