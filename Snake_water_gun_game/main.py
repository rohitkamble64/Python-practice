'''
1 - snake
-1 - water
0 - gun
'''
import random

computer = random.choice([1, -1, 0])
user = input("Enter your choice (snake, water, gun): ").lower()
userDict = {'snake': 1, 'water': -1, 'gun': 0}
you = userDict[user]

if (computer == you):
    print(f"Computer chose {computer}. It's a tie!")

else:
    if (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print(f"Computer chose {computer}. You lose!")
    else:
        print(f"Computer chose {computer}. You win!")
