""" # prompt user for coin
valid_coins = [5, 10, 25]
due = 50

while True:
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in valid_coins:
        while due > 0:
            due =- inserted_coin
            print(f"Amount Due: {due}")50
# print amount due after each time a coin has been inserted

# if amount inserted is at least 50 tell user how much change is owed
 """

""" def main():
    cost = 50
    inserted_coin = 0
    inserted_coin += inserted_coin
    inserted_coin = int(input("Insert coin: "))

    if is_valid(inserted_coin):
        cost = 50
        while inserted_coin < cost:
            cost -= inserted_coin
            print(f"Amount Due:{cost}")
        print(f"Change Owed:{50 - cost}")

def is_valid(c):
    valid = [5, 10, 25]
    return True if c in valid else False

main()
 """
""" cost = 50

while True:
    inserted_coin = int(input("Insert coin: "))

    if inserted_coin in [5, 10, 25]:

        cost -= inserted_coin

        if cost < 0:
            print(f"Change owed: {cost * -1} ")

        elif cost == 0:
            print("Change owed: 0")

        else:
            print(f"Amount due: {cost} ") """


valid_coins = [5, 10, 25,]
cost = 50

print("Amount Due: 50")

while True:
    inserted_coin = int(input("Insert coin: "))

    if inserted_coin in valid_coins:
        # calculate change if coin is valid
        cost -= inserted_coin

        if cost < 0:
            print(f"Change Owed: {cost * -1}")
            break

        elif cost == 0:
            print(f"Change Owed: 0")
            break

        else:
            print(f"Amount Due: {cost}")
    else:
        print("Amount Due: 50")