import random

def play():
    system_choice=random.choice(['r','p','s'])
    print(system_choice)
    user_choice=input(f"Enter your choise from - Rock(r),Paper(p),seasors(s):").lower()
    if (user_choice==system_choice):
        return ("It's tie,Please Try again :")# print("It's tie,Try again :")
    elif is_win(user_choice,system_choice):
        return ("You won the game :")
    return ("You lost it:")
    #p>r s>p r>s

def is_win(user,system):
    if (user=="p" and system=="r" or user=="s" and system=="p" or user=="r" and system=="s"):
        return (True)

print(play())