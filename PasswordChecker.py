from tkinter import *
window = Tk()


windowLabel = Label(window, text="Spooky Password Checker 1.0")
LowerLabel = Label(window, text="Check the following box if you want the password to include lowercase letters.")
UpperLabel = Label(window, text="Check the following box if you want the password to include uppercase letters.")
NumLabel = Label(window, text="Check the following box if you want the password to include numbers.")
windowLabel.grid(row = 0, column = 0)
LowerLabel.grid(row = 1, column = 0)
UpperLabel.grid(row = 2, column = 0)
NumLabel.grid(row = 3, column = 0)

window.mainloop()

#Flags for password
flagLower = False
flagUpper = False
flagNumeric = False
# Check if we are allowing lowercase letters : abc
print("Can your password contain lowercase letters?")
answer = input("Reply with \"yes\" or \"no\"")
if answer == "yes":
    flagLower = True
# Check if we are allowing uppercase letters : ABC
print("Can your password contain uppercase letter?")
answer = input("Reply with \"yes\" or \"no\"")
if answer == "yes":
    flagUpper = True
# Check if we are allowing numbers : 123
print("Can your password contain numbers?")
answer = input("Reply with \"yes\" or \"no\"")
if answer == "yes":
    flagNumeric = True
password = input("Please enter the password you have chosen.")
flagcount = 0
for index,character in enumerate(password):
    if not(flagLower):
        if character.islower():
            print("This password does not meet the requirements because it contains a lowercase letter at the ", index+1, " spot.")
            flagcount+=1
    if not(flagUpper):
        if character.isupper():
            print("This password does not meet the requirements because it contains an uppercase letter at the ", index+1, " spot.")
            flagcount+=1
    if not(flagNumeric):
        if character.isdigit():
            print("This password does not meet the requirements because it contains a number at the ", index+1, " spot.")
            flagcount+=1
if flagcount == 0:
    print("This password meets our criteria!")


        
