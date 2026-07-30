"""
Question:
Write a Python program to detect whether a comment is spam.
Consider the comment as spam if it contains any of the following words:
- "Make a lot of money"
- "Buy now"
- "Subscribe this"
- "Click this"
Otherwise, display that the comment is not spam.
""" 

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "click this"

message = input("enter Your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")

else:
    print("Not Spam")
