# This is a coding practice repo!

>>Statement: Its a multiplayer game, evryone gets a turn. When you get a turn you roll a die, you get a number from 1 to 6. If you get anything other than one then it get adds up in your score, which is intially set to zero. you can decide as much rolls as you want but if you get 1 the score becomes zero. the max score is 55 whoever hits 51 fist will be the # Winner

# Algorithm
1. generate a number btw 1-6
2. ask player if they wanna roll again or stop
    a. if stop : add and show the final score
        if score >= 55
            Winner
        if not 
            continue
    b. if no : roll the dice again
