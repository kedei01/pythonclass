import random

print("Welcome to Rock Paper Scissors!")
print("-------------------------------")

### Set up variables
cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["R", "P", "S"]


def checkForWinner(playerHand, computerHand):
    if (playerHand == "R" and computerHand == "P"):
        print("Sorry you lost :(")
        return "Cpu"
    elif (playerHand == "R" and computerHand == "S"):
        print("Congrats! You have won :)")
        return "Player"
    elif (playerHand == "S" and computerHand == "P"):
        print("Congrats! You win :)")
        return "Player"
    elif (playerHand == "S" and computerHand == "R"):
        print("Sorry, you lost!")
        return "Cpu"
    elif (playerHand == "P" and computerHand == "R"):
        print("Congrats! You win :)")
        return "Player"
    elif (playerHand == "P" and computerHand == "S"):
        print("Sorry, you lost!")
        return "Cpu"
    else:
        print("It's a tie, play again!")
        return "Tie"

# git init
 git add .
git commit -m "pythonclass"
# git remote add origin https://github.com/kedei01/pythonclass.git
# git push -u origin master or git push -f origin master
# ### Start game loop
# git push -f origin main
# git remote set-url origin https://github.com/kedei01/pythonclass.git
# $ git remote -v
while (playerScore != 3 and cpuScore != 3):
    ### Validate input
    while True:
        playerHand = input("\nPick a hand. R, P, or S: ")
        if (playerHand == "R" or playerHand == "P" or playerHand == "S"):
            break
        else:
            print("Invalid input. Try again.")

    ### Generate computer pick
    computerHand = random.choice(possibleHands)

    ### Print results
    print("Player hand: ", playerHand)
    print("Cpu hand: ", computerHand)
    result = checkForWinner(playerHand, computerHand)
    if (result == "Player"):
        playerScore += 1
    elif (result == "Cpu"):
        cpuScore += 1
    else:
        tieScore += 1
    print("Your score: ", playerScore, "CPU: ", cpuScore, "Ties: ", tieScore)

print("Game over! Thank you for playing :)")
