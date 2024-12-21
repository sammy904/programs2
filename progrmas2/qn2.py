print ("Welcome to Treasure Land")
a= input("choose a direction 'left' or 'right'")
if a== 'right':
    print("Game Over. You fell into a trap!")
else:
    b=input("you've reached a lake. Do you want to 'swim' or 'wait'?")
    if b=='swim':
        print("Game Over. You were attacked by crocodiles!")
    else:
        c= input("You see three doors: one 'red', one 'blue', and one 'yellow'. Which one do you choose? ")
        if c == "red":
            print("Game Over. You were burned by fire!")
        elif c == "blue":
            print("Game Over. You were eaten by beasts!")
        elif c == "yellow":
            print("Congratulations! You found the treasure! You Win!")
        else:
            print("Game Over. You chose a door that doesn't exist.")
