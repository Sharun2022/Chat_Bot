#list to store ordered pizzas 
order_list =['Spring Rolls', 'Mee Goreng', 'Pad Thai', 'Whole Duck']
#list to store pizza prices
order_cost = [5.00, 14.00, 17.00, 23.50]

cust_details = {'name':'Mark','phone':'0213345656', 'house': '45', 'street':'Harry','suburb': 'Howick'}

#print("Customer Name: {} \nCustomer Phone: {} \nCustomer Address: {} {} {}" .format( cust_details['name'], cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb']))

print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")


count = 0
for item in order_list:
    print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
    count = count + 1