#list to store ordered pizzas 
order_list =['Spring Rolls', 'Mee Goreng', 'Pad Thai', 'Whole Duck']
#list to store pizza prices
order_cost = [5.00, 14.00, 17.00, 23.50]


count = 0
for item in order_list:
    print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
    count = count + 1
