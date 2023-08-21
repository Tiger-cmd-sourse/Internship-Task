import random

u = 0
c = 0

def main():
    print("-" * 50)
    print("Hello, Welcome to Stone,Paper and Scissor Game")
    print("-" * 50)
    while u != 3 and c != 3:
        user_input = user_action()
        comp_input = comp_action()
        check_inputs(user_input, comp_input)
        
    if u == 3:
        print("\n Congratulation You won the Game!!!")
    elif c == 3:
        print("Oops you losed the Game ")
        print("Computer won the Game!!!")


# ask user to select Stone,Paper or Scissor
#user will have to enter stone or paper or scissor in text in the input field
def user_action():
    print("Choose option from the following: ")
    print("1)Stone")
    print("2)Paper")
    print("3)Scissor")
    user_input = input("Stone... Paper... Scissor... : ")
    user_input = user_input.lower()
    return user_input


# function to take computer random input form the list
def comp_action():
    Options = ["stone", "paper", "scissor"]
    comp_input = random.choice(Options)
    return comp_input


# to check both the inputs (the rules)
def check_inputs(user_input, comp_input):
    global u, c  #Global variables
    if user_input == "stone" and comp_input == "stone":
        print("It is a tie")

    elif user_input == "stone" and comp_input == "paper":
        c += 1
        print("Computer won his " + str(c) + " round!")
        
    elif user_input == "stone" and comp_input == "scissor":
        u += 1
        print("You won your " + str(u) + " round!")
        
    elif user_input == "paper" and comp_input == "stone":
        u += 1
        print("You won your " + str(u) + " round!")
        
    elif user_input == "paper" and comp_input == "paper":
        print("It is a tie!")

    elif user_input == "paper" and comp_input == "scissor":
        c += 1
        print("Computer won his " + str(c) + " round!")
        
    elif user_input == "scissor" and comp_input == "stone":
        c += 1
        print("Computer won his " + str(c) +" round!")
        
    elif user_input == "scissor" and comp_input == "paper":
        u += 1
        print("You won your " + str(u) + " round!")
        
    elif user_input == "scissor" and comp_input == "scissor":
        print("It is a tie")
    else:
        print("Invalid input. Please re-enter like stone or paper or scissor")


if __name__ == "__main__":
    main()
