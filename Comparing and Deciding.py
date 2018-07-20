amount = int(input("How many items have you brought? >>"))

if amount < 3:
    print("Buy some more!")
elif 3 <= amount <=5:
    print("Thanks!")
elif amount > 5:
    print("Discount for you!!!")
    
