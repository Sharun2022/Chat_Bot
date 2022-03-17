# Menu so that user can choose either delivery or click and collect

#Bug   - need to make it so that it only accepts 1 or 2

print ("Is your order for click and collect or delivery?")
print ("For click and collect please enter 1")
print ("For delivery please enter 2")
while True:
    try:
        delivery = int(input("Please enter a number "))
        if delivery >= 1 and delivery <= 2 :
            if delivery == 1:
                print ("Click and Collect") 
                break 

            elif delivery == 2:
                print ("Delivery")
                break
        else: 
            print ("The number must be 1 or 2")
    except ValueError:
        print ("That is not a valid number")
        print ("Please enter 1 or 2")