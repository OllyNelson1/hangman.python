import time

file = open("nrmeyiifkodnnoxp.txt","r")

real_password = file.read()
real_username = "14Nelsono"

file.close()

username = input("Username:")
password = input("Password:")

if password == real_password and username == real_username:
    time.sleep(1)
    print("Welcome Olly Nelson!!!")

else:
    time.sleep(1)
    print("Get out of here you hacker!!!")
    quit()

validation_code = input("Enter validation code >>")

length = len(validation_code)

if length == 17:
    time.sleep(1)
    print("Ok... it really is you!!!")
    

else:
    time.sleep(1)
    print("You either made a mistake or your a hacker...")
    quit()

time.sleep(1)
choice2 = input("What account do you want to see? >>")

if choice2 == "school":
    
    




