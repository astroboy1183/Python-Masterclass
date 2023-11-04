## Code might require optimization. Will come back later.

import random

attempts = [3, 5]

tries = 0


def check_if_gone_rogue(num_tries, call_func): ## function to keep in check the number of invalid entries by the user. This function is reused by two functions, hence a parameter called 'call_func'.
    if num_tries >= 10:
        print("You have been entering invalid values for a very long time now. Please enter a valid value or exit "  # 
              "the game. Press 'y' to continue or 'n' to exit")
        continue_or_not = input().lower()
        if continue_or_not == 'n' or continue_or_not == 'no':
            exit()
        elif continue_or_not == 'y' or continue_or_not == 'yes':
            if call_func == "will_play_game":
                evaluate_guess()
                return
            pass
            num_tries = 0
        else:
            h = 3
            while (1):
                continue_or_not = input(
                    f"You are crossing your limits by entering wrong values! Please be in your limits! You get {h} chances before you exit automatically. Enter a choice.")
                if continue_or_not != 'y' and continue_or_not != 'yes' and continue_or_not != 'n' and continue_or_not != 'no':
                    h -= 1
                    if h == 0:
                        print("Goodbye! Seems that you have gone mad!")
                        exit()
                    print(f"You have {h} chances remaining before you exit automatically.")

                else:
                    if continue_or_not == 'y' or continue_or_not == 'yes':
                        if call_func == "will_play_game":
                            num_tries = 0
                            evaluate_guess()
                            return
                        else:
                            break
                    else:
                        print("You have chosen to exit after so many attempts! GoodBye!")
                        exit()
                    # num_tries = 0


def get_difficulty():
    input_correct = False
    num_tries = 0

    while not input_correct:
        # num_tries=0

        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            num = attempts[1]
            input_correct = True
            num_tries = 0
        elif difficulty == 'hard':
            num = attempts[0]
            input_correct = True
            num_tries = 0
        else:
            print("Enter the correct difficulty. The value that you entered is invalid.")
            num_tries += 1
            check_if_gone_rogue(num_tries, "")

        # if num_tries >= 10:
        #     print("You have been entering invalid values for a very long time now. Please enter a valid value or exit "
        #           "the game. Press 'y' to continue or 'n' to exit")
        #     continue_or_not = input().lower()
        #     if continue_or_not == 'n' or continue_or_not == 'no':
        #         exit()
        #     elif continue_or_not == 'y' or continue_or_not == 'yes':
        #         pass
        #         num_tries = 0
        #     else:
        #         h = 3
        #         while (1):
        #             continue_or_not = input(
        #                 f"You are crossing your limits by entering wrong values! Please be in your limits! You get {h} chances before you exit automatically. Enter a choice.")
        #             if continue_or_not != 'y' and continue_or_not != 'yes' and continue_or_not != 'n' and continue_or_not != 'no':
        #                 h -= 1
        #                 if h == 0:
        #                     print("Goodbye! Seems that you have gone mad!")
        #                     exit()
        #                 print(f"You have {h} chances remaining before you exit automatically.")
        #
        #             else:
        #                 if continue_or_not == 'n' or continue_or_not == 'no':
        #                     print("You have chosen to exit after so many attempts! GoodBye!")
        #                     exit()
        #                 num_tries = 0
        #                 break

    return num


guess_correct = False


def evaluate_guess():
    global guess_correct
    print("Welcome to the Number Guessing Game!")
    chosen_random_number = random.randint(1, 100)
    num = get_difficulty()
    if num != 3 and num != 5:
        exit()
    while num != 0 and not guess_correct:
        guess = int(input("Make a guess:"))
        if guess > 100:
            print("Wrong entry. Please enter a number between 1 and 100(both included).")
        else:
            if guess > chosen_random_number:
                print(f"Number too high. \n Guess Again.\n You have {num - 1} attempts remaining.")
                num -= 1
            elif guess < chosen_random_number:
                print(f"Number too low.\n Guess Again.\n You have {num - 1} attempts remaining.")
                num -= 1
            else:
                print("You made the right guess.")
                guess_correct = True
    print(f"You exhausted all your attempts. You lost. The number was {chosen_random_number}")
    return


will_play_game = False

while not will_play_game:
    play_game = input("Do you want to play the number guessing game? Enter 'y' for yes and 'n' for no")
    if play_game == 'y' or play_game == 'yes':
        evaluate_guess()
    elif play_game == 'n' or play_game == 'no':
        exit()
    else:
        print("Enter a valid value!")
        tries += 1
        check_if_gone_rogue(tries, call_func="will_play_game")
