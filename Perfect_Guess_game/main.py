import random

n = random.randint(1,50)
a = 0
guesses = 0

while  (a != n):
    a= int(input("Guess a number:"))
    guesses +=1 
    if(a>=n):
        print("lower number please")
    
    else:
        print("Higher number please")
    
print(f"You have guessed the number {n} in {guesses} attempts")