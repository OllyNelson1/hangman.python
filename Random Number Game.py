import random

random_number = random.randint(1,100)
choice = None

while choice != random_number:

    choice = int(input("Choose a number between 1 and 100 >>"))

    if choice == random_number:
        print("Well done")
        break

    elif choice >= random_number:
        print("Too big")

    elif choice <= random_number:
        print("Too small")


