# List of Food names
food_names = ['Spring Rolls', 'Chicken Satay', 'Pork Belly', 'Teriyaki Chicken Sushi (8 Pack)', 'Chicken Curry', 
'Mee Goreng','Deep Fried Prawns','Nasi Goreng', 'Tom Yum Soup', 'Pad Thai', 
'Stir Fried Tofu with Rice', 'Whole Duck'
]
# lists of Food Prices
food_prices = [5.00, 7.50, 10.50, 11.50, 13.50, 14.00, 14.50, 15.00, 15.50, 17.00, 18.50, 23.50]

#list to store ordered Food 
order_list =[]
#list to store Food prices
order_cost = []

#list to store order cost

def menu():
    number_food = 12

    for count in range (number_food):
        print("{} {} ${:.2f}"  .format(count+1, food_names[count], food_prices[count]))

menu()

# Ask for total number of pizzas for order
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
        
print(num_food)

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

print(order_list)
print(order_cost)


# Countdown until all pizzas are ordered 



# Print order