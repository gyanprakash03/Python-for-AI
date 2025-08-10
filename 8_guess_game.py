from random import randint

class Number:

    def __init__(self, num):
        self.num = num

    def guess(self, num, i):
        if self.num == num:
            print(f"Congrats! You guessed the number in {i+1} attempt(s)")
            return True
        else:
            print("Oops! You guessed wrong")
            if self.num < num:
                print("Go Lower!")
            else:
                print("Go Higher!")
            return False
            
n = Number(randint(1, 100))

print("\n***Welcome to Guess Game. Guess a number from 1 to 100. You have 7 attempts***")

for i in range(7):
    num = int(input(f"\nAttempt {i+1}: "))
    check = n.guess(num, i)
    if check:
        break

else:
    print("\nNo more attempts left. Try again.\n")