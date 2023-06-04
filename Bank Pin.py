# Question 2:
# Write a Python program that emulates the high-street bank mechanism for checking a PIN. Keep taking input from the keyboard (see below) until it is identical to a password number which is hard coded by you in the program.
# To output a prompt and read:
# supplied pin = input ("Enter your PIN: ")
# Restrict the number of attempts to 3 (be sure to use a variable for that, we may wish to change it later), and output a suitable message for success and failure. Be sure to include the number of attempts in the message.



pin = input("Enter your PIN")
if pin == "1234":
    print("PIN is correct")
else:
    print("PIN is wrong, please try again")



