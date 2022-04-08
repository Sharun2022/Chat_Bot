

def check_string(question):
    while True:
        response = input(question) 
        x = response.isalpha()
        if x == False:
            print ("Input must only contain letters")
        else:
            return response.title()
            
    
question = "Please enter your name "
name = check_string(question)
print(name)