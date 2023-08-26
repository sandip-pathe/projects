import random


def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)
    
    return roll


while True:
    players = input("Enter Number of Players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter number between 2 and 4")
    
    else:
        print("Invalid number")


max_score = 50
players_scores = [0 for _ in range(players)]


while max(players_scores) < max_score:
    current_score = 0
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", players_scores[player_idx], "\n")
        

        while True:
            should_play = input("do you want to play (y)? ")
            if should_play.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("Its 1, try again")
                current_score = 0
                break
            else:
                current_score += value
                print("your Score is: ", current_score)

        players_scores[player_idx] += current_score
        print(players_scores[player_idx])
