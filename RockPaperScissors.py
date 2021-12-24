import random

gameChoices = ["rock","paper","scissors"]
continueGame = ["yes","no"]
quitGame = ''
playerChoice = ''

while quitGame != 'QUIT':
    while playerChoice not in gameChoices:
        playerChoice = str(input("input your choice for the game (rock,paper,scissors): "))
    computerChoice = random.choice(gameChoices)
    print("Computer Choice: " + computerChoice)
    if (playerChoice == computerChoice):
        print("Tie!!")
    if (playerChoice == 'rock' and computerChoice == 'paper'):
        print("You lose!!")
    if (playerChoice == 'rock' and computerChoice == 'scissors'):
        print("You win!!")
    if (playerChoice == 'paper' and computerChoice == 'rock'):
        print("You win!!")
    if (playerChoice == 'paper' and computerChoice == 'scissors'):
        print("You lose!!")
    if (playerChoice == 'scissors' and computerChoice == 'rock'):
        print("You lose!!")
    if (playerChoice == 'scissors' and computerChoice == 'paper'):
        print("You win!!")
    continueGame = str(input("Want to continue the game (yes/no)?: "))
    if continueGame != 'yes':
        quitGame = 'QUIT'
    else:
        playerChoice = ''

print('Nice playing the game with you!!!')
