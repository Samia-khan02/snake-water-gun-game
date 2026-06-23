import random

    # 1 for Snake
    # -1 for Water
    # 0 for Gun
userwin=0
compwin=0

while True:
    
    computer = random.choice([-1, 1, 0])

    user = input("Enter your choice (Snake, Water, Gun): ").lower()

    user_choice = {
        "snake": 1,
        "water": -1,
        "gun": 0
    }

    reverse_dict = {
        1: "snake",
        -1: "water",
        0: "gun"
    }

    ch = user_choice[user]

    print(f"\nYou chose {reverse_dict[ch]}")
    print(f"Computer chose {reverse_dict[computer]}\n")

    if computer == ch:
        print("DRAW")

    elif computer == -1 and ch == 1:
        print("You WIN!!!")
        userwin += 1

    elif computer == -1 and ch == 0:
        print("You LOSE!")
        compwin += 1

    elif computer == 1 and ch == -1:
        print("You LOSE!")
        compwin += 1

    elif computer == 1 and ch == 0:
        print("You WIN!!!")
        userwin += 1

    elif computer == 0 and ch == -1:
        print("You WIN!!!")
        userwin += 1

    elif computer == 0 and ch == 1:
        print("You LOSE!")
        compwin += 1

    else:
        print("Oops! Something went wrong.")

    print(f"Score -> You: {userwin} | Computer: {compwin}")


    print(" To play type : Yes \n Else type : no")
    choice=input("Enter your choice : ").lower()
    if choice=="yes":
        continue
    else:
        print("Come again next time!")
        break
