print("------NUMBER GUESSING GAME-------")
import random
comp=random.randint(1,100)
rounds=1
import random
n = random.randint(4,8)
print(f"You have only {n} attempts")
while rounds<=n:
    user=int(input("Enter your number(1-100): "))
    if user==comp:
        print(f"You guessed the number in {rounds} attempt.")
        print("You WON")
        break
    elif user>comp:
        print(f"Your number was greater in {rounds} attempt..")
    elif user<comp:
        print(f"Your number was small in {rounds} attempt.")
    else:
        print("You didn't guessed the number.")
        print("You LOOSE")
    rounds += 1
print(f"The original number is {comp}")