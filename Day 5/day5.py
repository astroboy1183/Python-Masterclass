#Password Generator

import random

print("Welcome to the PyPassword Generator.")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+}{|:<>?-/.,''\""
numbers = "1234567890"

print("How many letters would you like in your password?")
num_letters = int(input())

print("How many symbols would you like?")
num_symbols = int(input())

print("How many numbers would you like?")
num_numbers = int(input())

password = ""

for i in range(0,num_letters):
    password+=random.choice(letters)

for i in range(0,num_numbers):
    password+=random.choice(numbers)

for i in range(0,num_symbols):
    password+=random.choice(symbols)


final_password = ''.join(random.sample(password,len(password)))

print(final_password)