import time                             #importing time module
from datetime import datetime as dt     #importing datetime function from the datetime module


# Enter the path of your hosts file in your pc 
host_path = "c:\Windows\System32\drivers\etc\hosts" 

#Enter the localhost address for your system  
redirect = "127.0.0.1"

#Enter the website names that you want to block
website_list = ["facebook.com", "www.github.com", "github.com"]


while True:
#intializing the time duration for which the websites are required to be blocked 
    if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() <dt(dt.now().year, dt.now().month, dt.now().day, 18):
#In  (dt.now().day,9) 9 represents the hour like 9am


        with open(host_path, "r+") as file:                  #opening host_path in reading and writing mode
            content = file.read()                            #content variable contains the content of file 
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")   
                    #if the website in not present in the list  we write it in the file

        print("All the listed websites are blocked!!")
        break
    else:

        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:

                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()                               #Helps to resize the file according to text updated
        print("Websites are Unblocked! Have Fun!")
        break
