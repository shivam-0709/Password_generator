
# Password generartor


import string
import random


print ('Lets create password -- Please type "1 for easy", "2 for medium", "3 for hard" ')
letters = string.ascii_letters  # a-z, A-Z
numbers = string.digits         # 0-9
symbols = "!@#$%&*"            # basic symbols

while True:
    print ("Lets play the game")
    level = int(input ("Enter the level  "))
    clx = int(input("enter the value you want in password  "))

        
    # Combine all characters
    all_chars = letters + numbers + symbols
    letnum = letters + numbers
    password = ""

    for i in range (clx):
        if level == 1:
            password = password + random.choice(letters)
        elif level == 2:
            password = password + random.choice(letnum)
        elif level == 3:
            password = password + random.choice(all_chars)
        else:
            print ('Please enter the level as 1,2,3 only. Try again')
            break
    print(password)

    again = input("wanna play again 'Press y for Yes'  ")
    if again == 'y':
        continue

    else:
        break
        


print (f"Here is the password {password}") 
        







