# A bot for ordering food online

from asyncio.windows_events import INFINITE
from cmath import inf
import sys
import random
from random import randint

# Constants
LOW = 1  # LOW equals 1
HIGH = 2  # HIGH equals 2
PH_LOW = 7  # PH_LOW equals 7
PH_HIGH = 10  # PH_HIGH equals 10

# List of random names
names = ["George", "Phoebe", "Sally",  "Michael",
"Denise", "Ellen", "Moana", "Duncan", "Louis", "Danny"]

# List of Food names
food_names = ['Spring Rolls', 'Chicken Satay', 'Pork Belly',
'Teriyaki Chicken Sushi (8 Pack)', 'Chicken Curry',
'Mee Goreng', 'Deep Fried Prawns', 'Nasi Goreng', 'Tom Yum Soup', 'Pad Thai',
'Stir Fried Tofu with Rice', 'Whole Duck']

# List of Food Prices
food_prices = [5.00, 7.50, 10.50, 11.50, 13.50, 14.00, 14.50,
15.00, 15.50, 17.00, 18.50, 23.50]

# List to store ordered Food
order_list = []
# List to store Food prices
order_cost = []

# Customer details dictionary
customer_details = {}


# Validates inputs to check if they are blank
# Takes question as parameter
# Returns response in title class if valid
def not_blank(question):
    valid = False
    while not valid:  # While not false
        response = input(question)  # Asks for input (string)
        if response != "":
            return response.title()
            # if response not blank, it returns response in title class
        else:
            print("This cannont be blank")  # Prints error message


# Validates inputs to check if they are a string
# Takes question as parameter
# Returns response in title class if valid
def check_string(question):
    while True:  # Sets up Loop
        response = input(question)  # Asks for input (string)
        x = response.isalpha()
        # Checks that input in alphebetical and sets x to True if alphas
        if x == False:  # if x is False prints error message
            print ("Input must only contain letters")  # Prints message
        else:
            return response.title()  # if True returns response in title class


# Validates inputs to check if they an integer
# Takes question as parameter
def val_int(low, high, question):
    # Defines code as val_int with low, high, question as parameter
    while True:  # sets up while loop
        try:  # While the function is true
            num = int(input(question))  # Asks question
            if num >= low and num <= high:
            # If input is greater or equal to low (1) and less than or equal to high (2)
                return num  # Returns and accepts input
            else:  # If input is not the above
                print(f"The number must be between {low} and {high}")
                # Asks for input again
        except ValueError:
                print ("That is not a valid number")  # Prints error message


# Validates input to check if they are a number
# Takes question as parameter
def check_phone(question, PH_LOW, PH_HIGH):
    # Defines code as check_phone with question, PH_LOW, PH_HIGH as parameter
    while True:  # Sets up while loop
        try:  # While the function is true
            num = int(input(question))  # Asks question as parameter
            test_num = num  # Input equals variable
            count = 0  # Count set as 0
            while test_num > 0:  # While input is greater than 0
                test_num = test_num//10
                # test_num is equal to test_num divided by 10
                count = count + 1  # Adds 1 to count
            if count >= PH_LOW and count <= PH_HIGH:
            # If count is greater or equal to PH_LOW and less than or equal to PH_HIGH
                return str(num)  # Returns and accepts input
            else:  # If input is not the above
                print("NZ phone numbers have between 7 and 10 digits")
                # Prints message that number must be between 7 and 10 digits
        except ValueError:
            print("Please enter a number ")  # Prints error message


# Welcome message with random name
def welcome():  # Defines following code as welcome
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0, 9)
    # Name of person is randomised
    name = (names[num])  # Name will be chosen by their number
    print("*** Welcome to the Online Chat Bot ***")
    # Prints Welcome to the Online Chat Bot with asterisks
    print("*** My name is", name, "***")
    # Prints my name is (random name from list) with asterisks
    print("*** I will be here to help you order your delicious food online ***")
    # Prints message that they will helping the user make their order


# Menu for click and collect or delivery
def order_type():  # Defines following code as order_type
    del_pick = ""  # del_pick equals input
    question = (f"Please enter a number between {LOW} and {HIGH} ")
    # Asks user to enter a number between 1 and 2
    print ("Is your order for click and collect or delivery?")
    # Prints message
    print ("For click and collect please enter 1")  # Prints message
    print ("For delivery please enter 2")
    # Prints message to user to indicate that Delivery equals to input (2)
    delivery = val_int(LOW, HIGH, question)  # Delivery equals validated input
    if delivery == 1:  # If Delivery equals input (1)
        print ("Click and Collect")  # Prints "Click and Collect"
        del_pick = "Click and Collect"  # del_pick equals Click and Collect
        click_collect()  # click_collect function
    elif delivery == 2:  # If Delivery equals input (2)
        print ("Delivery")  # Prints "Delivery"
        delivery_info()  # delivery_info function
        del_pick = "Delivery"  # del_pick equals Delivery
    return del_pick  # Returns and accepts inputs


# Click and Collect information - name and phone number
def click_collect():  # Defines following code as click_collect
    question = ("Please enter your name ")  # Asks user to enter their name
    customer_details['name'] = check_string(question)
    # Validates the input of customer name
    print (customer_details['name'])  # Prints customer's name

    question = ("Please enter your phone number ")
    # Asks user to enter their phone number
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # Validates the input of phone
    print (customer_details['phone'])  # Prints customer's phone number


# Delivery information - name address and phone number
def delivery_info():  # Defines following code as delivery_info
    question = ("Please enter your name ")  # Asks user to enter their name
    customer_details['name'] = check_string(question)
    # Validates the input of customer name
    print (customer_details['name'])  # Prints customer's name

    question = ("Please enter your phone number ")
    # Asks user to enter their phone number
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # Validates input of customer phone number
    print (customer_details['phone'])  # Prints customer phone number

    question = ("Please enter your house number ")
    # Asks user to enter their house number
    customer_details['house'] = not_blank(question)
    # Validates customer house number
    print (customer_details['house'])  # Prints house number

    question = ("Please enter your street name ")
    # Asks user to enter their street name
    customer_details['street'] = check_string(question)
    # Validates the input of street name
    print (customer_details['street'])  # Prints street name

    question = ("Please enter your suburb ")  # Asks user to enter their suburb
    customer_details['suburb'] = check_string(question)
    # Validates the input of suburb
    print (customer_details['suburb'])  # Prints customer's suburb


#  Food menu
def menu():  # Defines following code as menu
    number_food = 12  # Sets there are 12 foods on the menu
    for count in range(number_food):  # For food(s) ranged between 1 and 12
        print("{} {} ${:.2f}"  .format(count+1, food_names[count], food_prices[count]))
        # Print the food menu with prices


#  Food order - menu - print each food ordered with cost
def order_food():  # Defines following code as order_food
    # Ask for total number of pizzas for order
    num_food = 0  # num_food equals 0
    NUM_LOW = 1  # Set Constant as 1
    NUM_HIGH = 20  # Set Constant as 20
    MENU_LOW = 1  # Set Constant as 1
    MENU_HIGH = 12  # Set Constant as 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    # Asks user to enter number between 1 and 20
    print("How many food(s) do you want to order?")
    # Prints how many food(s) do you want to order?
    num_food = val_int(NUM_LOW, NUM_HIGH, question)
    # num_food equals validated input

# Choose food from menu
    for item in range(num_food):  # For food(s) between 1 and 12
        while num_food > 0:  # While input is greater than 0
            print("Please choose your food(s) by entering the number from the menu")
    # Prints Please choose your food(s) by entering the number from the menu
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            # Asks user to enter a number between 1 and 12
            food_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            # food_ordered equals validated input
            food_ordered = food_ordered - 1
            # food_ordered equals food_ordered minus 1
            order_list.append(food_names[food_ordered])
            # Food names get added to order list
            order_cost.append(food_prices[food_ordered])
            # Food prices get added to order cost
            print("{} ${:.2f}" .format(food_names[food_ordered], food_prices[food_ordered]))
            # Print food(s) ordered with prices
            num_food = num_food - 1
            # num_food equals num_food minus 1


# Print order out -
# Inc if order is delievery/click & collect and names and prices of each food
# Total cost including any delivery charge
# Takes del_pick as parameter
def print_order(del_pick):
    # Defines code as print_order(del_pick) with parameter
    print()  # print blank spot
    total_cost = sum(order_cost)  # The total cost (Adds up all food ordered)
    print ("Customer Details")  # Print "Customer Details"
    if del_pick == "Click and Collect":
        # if delivery type was Click and Collect
        print ("Your Order is for Click and Collect")
        # Print your order is ready for click and collect
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
        # Prints customers name and customers phone
    elif del_pick == "Delivery":  # if pickup type = delivery
        print ("Your Order is for Delivery")
        # print your order is ready for delivery
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
        # print customers name, phone, address, house etc.
    print()  # Print blank space
    print("Your Order Details")  # Print your order is ready
    count = 0  # Set count to 0
    for item in order_list:  # for the items in the order list
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        # Print customers order and cost
        count = count + 1  # Adds 1 to count
    print()  # Print blank space
    if del_pick == "Delivery":  # If input equals Delivery
        if len(order_list) >= 5:
            # If number of food ordered is more than or equal to 5
            print ("Your order will be delievered for free")
            # Prints message informing the customer their delivery fee is free
        elif len(order_list) < 5:  # If number of food ordered is less than 5
            print ("There is an additional $9.00 delivery charge")
            # Prints message
            total_cost = total_cost + 9
            # Adds $9 to the total cost of food ordered
    print("Total Order Cost")  # Prints Total Order Cost
    print(f"${total_cost:.2f}")  # Prints the total cost in $
    if del_pick == "Click and Collect":  # If input equals Click and Collect
        print("Thank you for your order, we'll let you know when it's ready")
        # Prints message
    elif del_pick == "Delivery":  # Else if input equals delivery
        print ("Thank you for your order, it will be delievered soon")
        # Prints message

# Ability to cancel or proceed with order
# Asks user to confirm their order
# Asks user to enter 1 or 2 to confirm or cancel


def confirm_cancel():  # Defines the following code as confirm_cancel
    question = (f"Enter a number between {LOW} and {HIGH} ")
    # Asks user to enter number between 1 and 2
    print ("Please Confirm Your Order")  # Prints Please Confirm Your Order
    print ("To confirm please enter 1")  # Prints To Confirm Please Enter 1
    print ("To cancel please enter 2")  # Prints To Cancel Please Enter 2

# Order for confirmation
# If confirm equals 1
# Order is confirmed with message
    confirm = val_int(LOW, HIGH, question)  # Confirm equals validated input
    if confirm == 1:  # If input equals 1
        print ("Order Confirmed")  # Prints Order Confirmed
        print ("Your order has been sent to our kitchen")
        # Prints Your order has been sent to our kitchen
        print ("Your delicious food will be with you shortly")
        # Prints Your Delicious Food will be with you shortly
        new_exit()  # Moves on to option for new order or exit the bot

# Order for cancellation
# Else if confirm equals 2
# Order is cancelled with message
    elif confirm == 2:  # If input equals 2
        print ("Your Order has been Cancelled")
        # Prints order cancellation message
        print ("You can restart your order or exit the BOT")
        # Prints that they can restart the order or exit the bot
        new_exit()  # Moves on to option for new order or exit the bot

# Option for new order or to exit
# Asks user to enter between 1 and 2
# (1) equals start another order
# (2) equals exit the bot


def new_exit():  # Defines the following code as new_exit
    question = (f"Enter a number between {LOW} and {HIGH} ")
    # Asks user to enter between 1 or 2
    print ("Do you want to start another order? or exit?")
    # Prints do you want to start another order? or exit?
    print ("To start another order enter 1")
    # Prints to start another order, they must enter 1
    print ("To exit the BOT enter 2")
    # Prints to exit the bot, they must enter 2
    confirm = val_int(LOW, HIGH, question)  # Confirm equals validated input

    if confirm == 1:  # If input equals 1
        print ("New Order")  # Prints New Order
        order_list.clear()  # Clears the list of food names
        order_cost.clear()  # Clears the cost of foods
        customer_details.clear()  # Clears the previous customer details
        main()  # Main Function

    elif confirm == 2:  # Else if confirm input equals 2
        print("Exit")  # Prints 'Exit' message
        order_list.clear()  # Clears the list of food names
        order_cost.clear()  # Clears the costs of foods
        customer_details.clear()  # Clears the previous customer details
        sys.exit()  # Exits the bot fully

# Main Function


def main():  # Define the following code as main
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_food()
    print_order(del_pick)
    confirm_cancel()

main()
