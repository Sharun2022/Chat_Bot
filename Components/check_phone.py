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
                return num
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number ")


# Lowest amount of digits is 7
ph_low = 7
# Highest amount of digits is 10
ph_high = 10
question = ("Please enter your phone number ")

phone = check_phone(question, ph_low, ph_high)
print(phone)