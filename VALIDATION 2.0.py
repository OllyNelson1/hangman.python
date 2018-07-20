age_int = None

while age_int == None:

    try:
        age = input("Enter an age >>")
        age_int = int(age)
    except ValueError:
        age_int = None
        print("That's not an age!")

print(age_int,"is a nice age!")

#"except" runs if any error occurs; even syntax. This means we have to put the error we want it to catch next to it ("ValueError")

#validating if the entered value is a number or not 
