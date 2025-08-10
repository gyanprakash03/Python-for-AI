import random

options = ["stone", "paper", "scissors"]
user = 0
computer = 0

i = 0 
while i < 3:
    print(f"\n-------------------ROUND {i+1}-------------------\n")

    opt1 = int(input("Choose an option (0 : Stone | 1: Paper | 2: Scissors) : "))
    opt2 = random.choice(options)

    if opt1 not in range(0, 3):
        print("Option invalid! Choose again")
        continue

    if options[opt1] == opt2:
        print(f"You chose {options[opt1]}")
        print(f"Computer chose {opt2}")
        print("No result")

    elif opt1 == 0:
        if opt2 == "paper":
            print(f"You chose {options[opt1]}")
            print(f"Computer chose {opt2}")
            print("You lost!")
            computer += 1
        
        if opt2 == "scissors":
            print(f"You chose {options[opt1]}")
            print(f"Computer chose {opt2}")
            print("You won!")
            user += 1         

    elif opt1 == 1: 
        if opt2 == "scissors":
            print(f"You chose {options[opt1]}")
            print(f"Computer chose {opt2}")
            print("You lost!")
            computer += 1

        if opt2 == "stone":
            print(f"You chose {options[opt1]}")
            print(f"Computer chose {opt2}")
            print("You won!")
            user += 1

    elif opt1 == 2:
        if opt2 == "paper":
            print(f"You chose {options[opt1]}")
            print(f"Computer chose {opt2}")
            print("You won!")
            user += 1

        if opt2 == "stone":
            print(f"You chose {options[opt1]}")
            print(f"Computer chose {opt2}")
            print("You lost!")
            computer += 1

    i += 1 

print(f"\nUser score : {user}")
print(f"Computer score : {computer}")

with open("6_database.txt", "r+") as f:
    currStreak = int(f.readline())
    maxStreak = int(f.readline())

    if user > computer:
        print("You won the game!")
        currStreak += 1
        if currStreak > maxStreak:
            maxStreak = currStreak
            print(f"Congrats! You have a new best winning streak of {maxStreak}")

    elif user < computer:
        print("You lost the game. Try again")
        currStreak = 0

    else:
        print("Game tied")

    f.seek(0)
    f.writelines([str(currStreak) + "\n", str(maxStreak) + "\n"])


print("\n-------------------GAME OVER-------------------\n")
