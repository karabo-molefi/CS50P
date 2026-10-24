fruit = {
    "Apple": 130,
    "Avocado" : 50,
    "Sweet Cherries" : 100,
    "Kiwifruit" : 90,
    "Pear" : 100,
}

user_input = input("Item: ").title()

if user_input in fruit:
    print(f"Calories: {fruit[user_input]}")
else:
    None