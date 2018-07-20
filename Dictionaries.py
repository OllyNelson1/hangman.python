##age = {}
##
##age["Paul"] = 48
##age["Olly"] = 15
##age["Jemie"] = 13
##age["Evie"] = 10
##age["Jo"] = 40
##
##print(age)

#Puts all of the peices of data in the "age" dictionary in alphabetical order.
#So "Jemie" is first. Then "Jo" and so on.
#Works like a list

repeat = "T"
dictionary = {}

while repeat == "T":

    name = input("Enter your name >>")

    age_int = None

    while age_int == None:

        try:
            age = input("Enter your age >>")
            age_int = int(age)
        except ValueError:
            age_int = None
            print("That's not an age!")

    dictionary[name] = age

    repeat = input("Do you want to enter some more data? (T/F) >>")

print("Your database is:",dictionary)
    
