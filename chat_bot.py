# A bot for ordering food online

from cmath import inf
import sys
import random
from random import randint

# Constants
LOW = 1
HIGH = 2
ph_low = 7
ph_high = 10

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
order_list =[]
# List to store Food prices
order_cost = []

# Customer details dictionary
customer_details = {}

# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannont be blank")

def check_string(question):
    while True:
        response = input(question) 
        x = response.isalpha()
        if x == False:
            print ("Input must only contain letters")
        else:
            return response.title()


# Validates inputs to check if they an integer
def val_int(low, high, question):
    while True: #sets up while loop
        try:
            num = int(input(question))
            if num >= low and num <= high :
                return num
            else:
                print(f"The number must be {low} or {high}")
        except ValueError:
                print ("That is not a valid number")

def check_phone(question, ph_low, ph_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0 
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= ph_low and count <= ph_high:
                return str(num)
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number ")

# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message
    Parameters: None
    Returns: None 
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to the Online Chat Bot ***")
    print("*** My name is",name,"***")
    print("*** I will be here to help you order your delicious food online ***")

# Menu for click and collect or delivery
def order_type():
    del_pick = ""
    question = (f"Please enter a number between {LOW} and {HIGH} ")
    print ("Is your order for click and collect or delivery?")
    print ("For click and collect please enter 1")
    print ("For delivery please enter 2")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Click and Collect")
        del_pick = "Click and Collect"
        click_collect() 
    elif delivery == 2:
        print ("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return del_pick

# Click and Collect information - name and phone number
def click_collect():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])


# Delivery information - name address and phone 
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    
    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = check_string(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = check_string(question)
    print (customer_details['suburb'])



# Food menu
def menu():
    number_food = 12
    for count in range (number_food):
        print("{} {} ${:.2f}"  .format(count+1, food_names[count], food_prices[count]))

# Food order - menu - print each food ordered with cost

def order_food():
    # Ask for total number of pizzas for order
    num_food = 0
    NUM_LOW = 1
    NUM_HIGH = inf
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("How many pizzas do you want to order?")
    num_food = val_int(NUM_LOW, NUM_HIGH, question)
 # Choose food from menu
    for item in range(num_food):
        while num_food > 0:
            print("Please choose your pizzas by entering the number from the menu")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            food_ordered = val_int(MENU_LOW, MENU_HIGH, question)     
            food_ordered = food_ordered - 1
            order_list.append(food_names[food_ordered])
            order_cost.append(food_prices[food_ordered])
            print("{} ${:.2f}" .format(food_names[food_ordered],food_prices[food_ordered]))
            num_food = num_food - 1

# Print order out -  including if order is delievery or click & collect and names and prices of each food - total cost including any delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "Click and Collect":    
        print ("Your Order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "Delivery":
        print ("Your Order is for Delivery")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count + 1
    print()
    if del_pick == "Delivery":
        if len(order_list) >= 5:
            print ("Your order will be delievered for free")
        elif len(order_list) <= 5:
            print ("There is an additional $9.00 delivery charge")
            total_cost = total_cost + 9
    print("Total Order Cost")
    print(f"${total_cost:.2f}")
    if del_pick == "Click and Collect":   
        print("Thank you for your order, we'll let you know when it's ready")
    elif del_pick == "Delivery":
        print ("Thank you for your order, it will be delievered soon")
    
# Ability to cancel or proceed with order 
def confirm_cancel():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please Confirm Your Order")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")
    
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("Order Confirmed")
        print ("Your order has been sent to our kitchen")
        print ("Your delicious Pizza will be with you shortly") 
        new_exit()
                     

    elif confirm == 2:
        print ("Your Order has been Cancelled")
        print ("You can restart your order or exit the BOT")
        new_exit()
                  

    


# Option for new order or to exit
def new_exit():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Do you want to start another order? or exit?")
    print ("To start another order enter 1")
    print ("To exit the BOT enter 2")
    confirm = val_int(LOW, HIGH, question)
       
    if confirm == 1:
        print ("New Order")  
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()
                

    elif confirm == 2:
        print("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()
            
# Main Function
def main():  
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