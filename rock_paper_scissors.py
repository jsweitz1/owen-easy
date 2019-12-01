

# we're going to play 3 rounds of rock paper scissors!
# first let's set up some things

import random
gamelist = ["Rock", "Paper", "Scissors"]


def play_game(user_input):
    index = random.randint(0,2)
    computer_guess = gamelist[index]
    count = 0
    wins = 0

    while count < 3:

        if user_input.lower() == "rock":
            if computer_guess == "Rock":
                print("Computer guessed rock, go again")
            elif computer_guess == "Paper":
                print("Computer guessed paper. Paper beats rock. Computer wins this round!")
                count += 1
            elif computer_guess == "Scissors":
                print("Computer guessed scissors. Rock beats scissors. You win this round!")
                count += 1
                wins += 1
        elif user_input.lower() == "paper":
            if computer_guess == "Rock":
                print("Computer guessed rock. Paper beats rock. You win this round!")
                count += 1
                wins += 1
            elif computer_guess == "Paper":
                print("Computer guessed paper, go again")
            elif computer_guess == "Scissors":
                print("Computer guessed scissors. Scissors beats paper. Computer wins this round!")
                count += 1
        elif user_input.lower() == "scissors":
            if computer_guess == "Rock":
                print("Computer guessed rock. Rock beats scissors. Computer wins this round!")
                count += 1
            elif computer_guess == "Paper":
                print("Computer guessed paper. Scissors beats paper. You win this round!")
                count += 1
                wins += 1
            elif computer_guess == "Scissors":
                print("computer guessed paper, go again")
        else:
            print("There was a problem with your input, go again")



play_game(input("Rock Paper Scissors! What do you pick?  ")


print("Game over!\nYou won " + str(wins) + "out of 3")

if count == 2 or 3:
    print("Great Job!")
else:
    print("You'll do better next time!")