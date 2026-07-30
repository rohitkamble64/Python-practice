"""
Question:
Write a Python program to check the length of a username.

If the username contains fewer than 8 characters,
display an appropriate message.
Otherwise, indicate that the username is valid.
"""

username = input("Enter your Username: ")

if(len(username)<8):
    print("Yor username contains less than 8 characters")

else:
    print("All is well")
