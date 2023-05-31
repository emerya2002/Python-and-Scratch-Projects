import random
import string
import array

## create list of characters
digits = string.digits
letters = string.ascii_letters
symbols = '!@#$%^&*,_-+=;:<>?'

char = list(letters)

def randomPassword():
    intro = input('Would you like to use the Random Password Generator? (Enter Yes or No): ')
    if intro in ('Yes', 'yes', 'YES'):
        print('Awesome! Please follow the instructions below')
    
        ## determine the length of the password
        len = int(input("How long would you like your password: (Enter any number):"))
        
        ## determine if you want numbers in the password
        qDigits = input("Would you like to include numbers?: (Enter Yes or No):")
        if qDigits == 'Yes' or 'yes' or 'YES':
            char = list(letters + digits)
        
        ## determine if you want symbols in the password
        qSymbols = input("Would you like to include symbols?: (Enter Yes or No):")
        if qSymbols == 'Yes' or 'yes' or 'YES':
            char = list(letters + digits + symbols)
                    
        else:
            char = list(letters)
            ## determine if you want symbols in the password
            qSymbols = input("Would you like to include symbols?: (Enter Yes or No):")
            if qSymbols == 'No' or 'NO' or 'no':
                char = list(letters + symbols)
       
    
        ## Randomize the list of characters
        random.shuffle(char)
        
        ## Select characters randomly
        password = []
        for i in range(len):
            password.append(random.choice(char))
        
        random.shuffle(password)
        print()
        print("Here is the Password: " + "".join(password))
        
    else:
        print('Ok! Bye')
        

    
randomPassword()
    