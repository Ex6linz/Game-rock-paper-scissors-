import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock , paper , scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_images[choice])


comp = random.randint(0, 2)
print("Computer chose: ")
print(game_images[comp])

print(f"Computer chose {comp}")
if choice > 2:
    print("Invalid number")
elif choice == 0 and comp == 2:
    print("You wins!")
elif choice == 0 and comp == 1:
    print("Sorry , You lose play again")
elif choice == 0 and comp == 0:
    print("It's a draw")
elif comp > choice:
    print("You lose")
elif choice > comp:
    print("You win!")
elif comp == choice:
    print("It's a draw")




