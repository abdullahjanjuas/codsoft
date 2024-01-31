#A Password Generator using Python
import random

#Characters to be chosen from the string for password generation
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()*&%$#@!"

while True:
    p_length = int(input("What length do you want for your password?"))
    p_count = int(input("How many passwords do you wish to generate?"))
    for x in range(p_count):
        password = ""
        for x in range(p_length):
            password_char = random.choice(chars)
            password += password_char
        print("Here is your password: " + password)
    conti = input("\nDo you wish to continue? Y/N\n")
    if(conti != 'Y'):
        print("Bye!")
        break 
    
        
    