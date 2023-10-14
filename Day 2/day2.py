print("Welcome to the tip Calculator.\nWhat was the total bill?")
total_bill = float(input())
print("What percentage tip would you like to give?")
tip_percentage = float(input())
print("How many people split the bill?")
num = int(input())

each = (total_bill + ((tip_percentage / 100) * total_bill)) / num

print("Each person should pay:\n ", round(each, 2))