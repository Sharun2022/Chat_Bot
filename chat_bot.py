# A bot for ordering food online

import sys
import random
from random import randint

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

#list to store ordered Food 
order_list =[]
#list to store Food prices
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



# Validates inputs to check if they an integer
def val_int(low, high, question):
        while True:
            try:
                num = int(input(question))
                if num >= low and num <= high :
                    return num
            except ValueError:
                print ("That is not a valid number")
                print (f"Please enter a number between {low} and {high}")



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
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Pickup")
        del_pick = "Pickup"
        click_collect() 
    elif delivery == 2:
        print ("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return del_pick

# Click and Collect information - name and phone number
def click_collect():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    print("You will recieve a text, when the food is ready for pickup")

# Delivery information - name address and phone 
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    
    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])




# Food menu
def menu():
    number_food = 12
    for count in range (number_food):
        print("{} {} ${:.2f}"  .format(count+1, food_names[count], food_prices[count]))

# Food order - menu - print each food ordered with cost

def order_food():
    # Ask for total number of food for order
    num_food = 0 
    while True:
        try:
            num_food = int(input("How many different food(s) would you like to order? "))
            if num_food >=1: 
                break
            else:
                print("Please enter a natural number")
        except ValueError:
            print("That is not a valid number")   
            print("Please enter a valid natural number ")
        #Choose food from menu
    for item in range(num_food):
        while num_food > 0:
            while True:
                try:
                    food_ordered = int(input("Please choose your food(s) by entering the number from the menu "))
                    if food_ordered >= 1 and food_ordered <= 12:
                        break
                    else:
                        print("Your food order must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")   
                    print("Please enter a number between 1 and 12") 
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
    if del_pick == "Pickup":
        print ("Your Order is for Pickup")
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
    if del_pick == "Pickup":   
        print("Thank you for your order, we'll let you know when it's ready")
    elif del_pick == "Delivery":
        print ("Thank you for your order, it will be delievered soon")
    
# Ability to cancel or proceed with order 
def confirm_cancel():
    LOW = 1
    HIGH = 2
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
    LOW = 1
    HIGH = 2
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