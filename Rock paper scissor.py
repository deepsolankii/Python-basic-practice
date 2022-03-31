# Rock Paper Scissor game


import random

print("Input number of times you want to play Rock,Paper,Scissor:")
n = int(input())
game = 1
com_win = 0
play_win = 0
Tie = 0

# Creating a game loop.
while game <= n:
    choice = ["Rock", "Paper", "Scissor"]
    computer = random.choice(choice)
    player = input("Rock, Paper Or Scissor:\n").capitalize()
    if player not in choice:
        print("Error , Please choose from given 3 choice\n")
    else:
        game += 1
        if player == computer:
            print(f"Computer : {computer} \n Player : {player} \n It's a tie!!!")
            Tie += 1
        elif (player == "Rock" and computer == "Scissor") or (player == "Paper" and computer == "Rock") or (
                player == "Scissor" and computer == "Paper"):
            print(f"Computer : {computer} \n Player : {player} \n Player wins!!")
            play_win += 1
        else:
            print(f"Computer : {computer} \n Player : {player} \n Computer wins!!")
            com_win += 1

# printing the results
print(f"Number of games Tied :{Tie} \n")
print(f"Number of games Player won :{play_win} \n")
print(f"Number of games Computer won:{com_win} \n")
