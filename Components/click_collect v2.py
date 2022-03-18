#Bug - accepts blank input

print ("Please enter the click and collect information")

# Customer name
valid =  False
while not valid:
    name = input("Please enter your name ")
    if name != "":
        print (name)
        break

    else:
        print("Sorry this cannot be blank")


# Phone number
valid =  False
while not valid:
    phone = input("Please enter your phone number ")
    if phone != "":
        print (phone)
        break

    else:
        print("Sorry this cannot be blank") 

print ("You will recieve a text, when the food is ready for pickup")