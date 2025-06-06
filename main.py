print("Welcome to the Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
#todo: work out how much they need to pay based on their size choice
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill+=2
        if extra_cheese == "Y":
            bill+=1
elif size == "M":
    bill =20
    if pepperoni == "Y":
        bill+=2
        if extra_cheese == "Y":
            bill+=1
elif size == "L":
    bill =25
    if pepperoni == "Y":
        bill+=2
        if extra_cheese == "Y":
            bill+=1
else:
    print("You have chosen the wrong inputs")
#todo: work out how much to add on their bill based on their pepperoni choice
#todo: work out on the final amount based on whether they want extra cheese
print(f"Your final bill amount is: {bill}")