import random


def game():
    choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    rock = 0
    paper = 1
    scissors = 2

    p = rock < paper
    q = rock > scissors
    r = scissors > paper
    comp = random.random()
    if choose == 0:
        choose == 0

        choose < paper and choose > scissors
        if choose > cmp == paper == False:
            print("You lose,paper")
        elif choose > comp == scissors == False:
            print("Yeah, you win, scissors")
        else:
            print("It's a draw")

    if choose == 1:
        choose == 1
        comp == rock or comp == scissors
        choose > rock and choose < scissors
        if choose > comp == rock == True:
            print("Congratulations you win, rock")
        elif choose < comp == scissors == True:
            print("Sorry, you can play again and try win , scissors")
        else:
            print("It's a draw")

    if choose == 2:
        choose == 2
        comp == paper or comp == rock
        choose > paper and choose < rock
        if choose > comp == paper == True:
            print("Congratulation, you win")
        elif choose > rock == True:
            print("Sorry, you lose")
        else:
            print("Play again, it's a draw")


game()






