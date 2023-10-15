#Rock Paper Scissors game.

import random

while(1):
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
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
    you = int(input())
    Dict ={0:rock,1:paper,2:scissors}
    print(Dict[you])

    comp = random.randint(0,2)
    print(Dict[comp])

    if you <0 or you>=3:
        print("Invalid Input.")

    if you==comp:
        print("Draw!")
    elif you==0 and comp == 2:
        print("You Win!")
    elif you==2 and comp == 0:
        print("Comp Wins!")
    elif you>comp:
        print("You Win!")
    else:
        print("Comp Wins!")
