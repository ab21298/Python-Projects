import random

print("Welcome to Snake, Water, Gun Game")
c = True
while c:
    user_score = 0
    comp_score = 0
    total_chance = 5
    while total_chance != 0:
        user_choice = input("Enter Your Choice [s:snake, w:water, g:gun ] = ")
        comp_choice = random.choice(['s', 'w', 'g'])
        if user_choice == comp_choice:
            print("DRAW...")
            print(f"Your score = {user_score} and computer score = {comp_score}")
            total_chance = total_chance - 1
            print(f"Chance left = {total_chance}")
        if user_choice == 's' and comp_choice == 'w':
            print("You Win ")
            user_score = user_score + 1
            print(f"Your score = {user_score} and computer score = {comp_score}")
            total_chance = total_chance - 1
            print(f"Chance left = {total_chance}")
        elif user_choice == 'w' and comp_choice == 's':
            print("computer win")
            comp_score = comp_score + 1
            print(f"Your score = {user_score} and computer score = {comp_score}")
            total_chance = total_chance - 1
            print(f"Chance left = {total_chance}")
        if user_choice == 'w' and comp_choice == 'g':
            print("You Win ")
            user_score = user_score + 1
            print(f"Your score = {user_score} and computer score = {comp_score}")
            total_chance = total_chance - 1
            print(f"Chance left = {total_chance}")
        elif user_choice == 'g' and comp_choice == 'w':
            print("computer win")
            comp_score = comp_score + 1
            print(f"Your score = {user_score} and computer score = {comp_score}")
            total_chance = total_chance - 1
            print(f"Chance left = {total_chance}")
        if user_choice == 'g' and comp_choice == 's':
            print("You Win ")
            user_score = user_score + 1
            print(f"Your score = {user_score} and computer score = {comp_score}")
            total_chance = total_chance - 1
            print(f"Chance left = {total_chance}")
        elif user_choice == 's' and comp_choice == 'g':
            print("computer win")
            comp_score = comp_score + 1
            print(f"Your score = {user_score} and computer score = {comp_score}")
            total_chance = total_chance - 1
            print(f"Chance left = {total_chance}")
        else:
            print("Invalid Input")
    if user_score == comp_score:
        print("Match is end on a Draw")
    elif user_score > comp_score:
        print("Congratulation You win this game.")
    else:
        print("Sorry ! You Lose the Game Better Luck next Time")
    opt = input("Do You Want to play again [0 for no and 1 for yes] = ")
    if opt == '1':
        c = True
    else:
        c = False

print("Thanks for playing")
