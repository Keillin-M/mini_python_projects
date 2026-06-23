from art import logo

bid = {}
loop = True
print(logo)
while loop:
    key = input("What's your name? ")
    value = int(input("What's your bid? $"))
    bid[key] = value

    new_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 50)
    if new_bid == "no":
        loop = False

best = 0
winner = ""
for bidder in bid:
    if bid[bidder] > best:
        best = bid[bidder]
        winner = bidder
print(f"The winner is {winner} with a bid of ${best}")


