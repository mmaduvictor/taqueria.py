# Create a menu Dictionary
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# set total amount to 0
totalAmount = 0
# loop forever
while True:
    try:
        # getting user input
        item = input("item: ")
        # check if item is in dictionary
        if item in menu:
            totalAmount += menu[item]
            print("total: $", end= "")
            print(totalAmount)

    except EOFError:
        print()
        break

