# A bot for ordering food online

import sys
import random
from random import randint

# List of random names
names = ["George", "Phoebe", "Sally",  "Michael", "Denise", "Ellen", "Moana", "Duncan", "Louis", "Danny"]

# List of Food names
food_names = ['Spring Rolls', 'Chicken Satay', 'Pork Belly', 'Teriyaki Chicken Sushi (8 Pack)', 'Chicken Curry', 
'Mee Goreng','Deep Fried Prawns','Nasi Goreng', 'Tom Yum Soup', 'Pad Thai', 
'Stir Fried Tofu with Rice', 'Whole Duck']

# List of Food Prices
food_prices = [5.00, 7.50, 10.50, 11.50, 13.50, 14.00, 14.50, 15.00, 15.50, 17.00, 18.50, 23.50]


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


def order_type():
    print("Is your order for click and collect or delivery?")
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




def menu():
    number_food = 12

    for count in range (number_food):
        print("{} {} ${:.2f}"  .format(count+1, food_names[count], food_prices[count]))

menu()



def main():
    '''
    Purpose: To run all functions 
    a welcome message
    Parameters: None
    Returns: None 
    '''
    welcome()
    


main()