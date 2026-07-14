from dictionarylogo import logo
bids = {}
print(logo)
while True:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))

    bids[name] = price

    other = input("Are there any other bidders? (yes/no): ").lower()

    if other == "no":
        break

highest_bid = 0
winner = ""

for person in bids:
    bid = bids[person]

    if bid > highest_bid:
        highest_bid = bid
        winner = person

print(f"The winner is {winner} with a bid of ${highest_bid}.")

    