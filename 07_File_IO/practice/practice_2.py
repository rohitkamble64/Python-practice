import random 

def game():
    print("Welcome to highscore game...")
    score = random.randint(1, 100)
    #fetch the highscore

    with open("07_File_IO/practice/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print("Your score is: ", score)
    if(score>hiscore):
        with open("07_File_IO/practice/hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()