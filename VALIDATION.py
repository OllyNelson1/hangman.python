validation2 = "false"

while validation2 == "false":

    repeat = input("Do you want another go (T/F) >>")

    if repeat == "T" or repeat == "F":
        validation2 = "true"
        break

    elif repeat != "T" or repeat != "F":
        validation2 = "false"
        print("Invalid, try again")

print(repeat,"completed")


