##Day 9 - Silent Auction Program

print("Welcome to the silent auction program")

end = False
bids = {}  # empty dictionary to hold the names and their bids

while not end:
    name = input("Enter your name").lower()
    bid = int(input("Enter your bid"))
    bids[name] = bid  # adding their names and their bids
    next_person_available = input("Are there any other members in the auction? y or n").lower()
    if next_person_available == "n" or next_person_available == "no":
        end = True

# Things to do: validate input for next_person_available properly.

max_bid = 0

for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        bidder_with_max = bidder

print(f"Bidder with max bid is {bidder_with_max} and the bid is {max_bid}")




