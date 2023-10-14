print("Welcome to Treasure Island. Your mission is to find the treasure.")

print("Choose \"left\" or \"right\"")

first_step = input().lower()

if(first_step=="right"):
    print("Game Over.")
    exit()
else:
    print("Great! Proceed ahead.")

print("Choose \"swim\" or \"wait\"")
second_step = input().lower()
if(second_step=="swim"):
    print("Game Over.")
    exit()
else:
    print("Great! Proceed ahead.")

print("Which door?")

print("Choose \"Red\" , \"Blue \" or \"Yellow\"")
third_step = input().lower()

if(third_step=="yellow"):
    print("You Win!")
else:
    print("Game Over.")
    exit()

