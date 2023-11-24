from game_data import data
# from art import logo, vs
import random

num_of_entries = len(data)
score = 0


def check(user_input, other_inp, score):
    if user_input > other_inp:
        print("You won")
        score += 1
        return score
    else:
        print("You Lost")
        print(f"Your score is {score}")
        exit()


while 1:
    chosen_number = random.randint(0, num_of_entries - 1)
    print(data[chosen_number]['name'])
    first = data[chosen_number]['follower_count']
    first_name = data[chosen_number]['name']
    chosen_number = random.randint(0, num_of_entries - 1)
    print(data[chosen_number]['name'])
    second = data[chosen_number]['follower_count']
    second_name = data[chosen_number]['name']
    inp = (input(f"Enter A for {first_name} and B for {data[chosen_number]['name']}"))
    print(f"{first_name} - {first}")
    print(f"{second_name} - {second}")
    if inp == 'A' or inp == 'a':
        score = check(first, second, score)
    else:
        score = check(second, first, score)
