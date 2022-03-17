# Bugs
# Will only work for valid input "d" and "c"
#invalid input triggers else statement but program does not as for input again.

# Menu so that user can choose either delivery or click and collect 

print ("Do you want your order delivered or are you picking it up?")

print (" For delivery enter d")
print (" For click and collect enter c")

delivery = input()

if delivery == "d":
    print ("Delivery")

elif delivery == "c":
    print ("Click and Collect")

else:
    print ("That was not a valid input")