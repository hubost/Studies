import random
exit = False
user_points = 0
computer_points = 0
choose = "Choose rock, paper, scissors or exit:"
end = "Game ended. "
ywin = "You win!"
cwin = "Computer wins."
your = "Your input is "
comp = "Computer input is "
tie = ("It is a tie.")
while exit == False:
    options = ["rock","paper","scissors"]
    user_input = input(choose)
    computer_input = random.choice(options)
    if user_input == "exit" :
        print(end)
        print("Total score:"+str(int(user_points)))
        exit = True

    if  user_input == "rock":
        if computer_input == "rock":
            print(your + "rock")
            print(comp + "rock")
            print(tie)
        elif computer_input == "scissors":
            print(your + "rock")
            print(comp + "scissors")
            print(ywin)
            user_points = user_points + 1
        elif computer_input == "paper":
            print(your + "rock")
            print(comp + "paper")
            print(cwin)
    elif  user_input == "scissors":
        if computer_input == "scissors":
            print(your + "scissors")
            print(comp + "scissors")
            print(tie)
        elif computer_input == "paper":
            print(your + "scissors")
            print(comp + "paper")
            print(ywin)
            user_points = user_points + 1
        elif computer_input == "rock":
            print(your + "scissors")
            print(comp + "rock")
            print(cwin)
    elif  user_input== "paper":
        if computer_input == "paper":
            print(your + "paper")
            print(comp + "paper")
            print(tie)
        elif computer_input == "rock":
            print(your + "paper")
            print(comp + "rock")
            print(ywin)
            user_points = user_points + 1
        elif computer_input == "scissors":
            print(your + "paper")
            print(comp + "scissors")
            print(cwin)

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "exit":
        print("Invalid input.")
