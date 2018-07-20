repeat = "T"
validation = "false"
validation2 = "false"

print("Welcome to my pig latin encryptor and decryptor!")

while repeat == "T":

    validation = "false" 
    validation2 = "false"

    while validation == "false":

        choice = input("\nDo you want to encrypt or decrypt? >>")

        if choice == "encrypt" or choice == "decrypt":
            validation = "true"
            break

        elif choice != "encrypt" or choice != "decrypt":
            validation = "false"
            print("\nInvalid, try again")

    if choice == "encrypt":
        
        def igpay(word):
            
            if word[0] in "aeiou":
                
                word = (word + "way")
                print("\n    ",word,"\n")
            
            elif word[0] in "bcdfghjklmnpqrstvwxyz":
                first_letter = word[0]
                word = word[1:]
                word = (word + first_letter + "ay")
                print("\n    ",word,"\n")

    elif choice == "decrypt":
        
        def igpay(word):
            
            if word[-3] == "w" or word:

                word = word[:-3]
                print("\n    ",word,"\n")

            elif word[-3] != "w":
                
                if word[-2] == "a" and word[-1] == "y":
                    first_letter = word[-3]
                    word = word[:-2]
                    word = word.strip(first_letter)
                    word = (first_letter + word)
                    print("\n    ",word,"\n")
                    
                else:
                    print("That's not a pig latin word!!!\n")

            else:
                print("That's not a pig latin word!!!\n")
                
    if choice == "encrypt":
        
        word = input("\nPlease enter a word to encrypt to pig latin >>")
        igpay(word)

    elif choice == "decrypt":

        word = input("\nPlease enter a pig latin word to decrypt to english >>")
        igpay(word)

    while validation2 == "false":

        repeat = input("Do you want another go (T/F) >>")

        if repeat == "T" or repeat == "F":
            validation2 = "true"
            break

        elif repeat != "T" or repeat != "F":
            validation2 = "false"
            print("\nInvalid, try again\n")

print("\nThank you for using my pig latin encryptor/decryptor!!!\n")

