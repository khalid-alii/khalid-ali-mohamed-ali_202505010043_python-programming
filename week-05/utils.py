def calculate_total(coffee, tea, sandwich):
    coffeePrice = 8.50
    teaPrice = 6.00
    sandwichPrice = 12.00
    
    total = (coffee * coffeePrice) + (tea * teaPrice) + (sandwich * sandwichPrice)
    
    return total


def print_receipt(name, coffee_qty, tea_qty, sandwich_qty, total_amount):
    print("\n===== RECEIPT =====")
    print(f"Customer : {name}")
    print(f"Coffee   : {coffee_qty}")
    print(f"Tea      : {tea_qty}")
    print(f"Sandwich : {sandwich_qty}")
    print("-------------------")
    print(f"Total    : RM {total_amount:.2f}")
    print("===================")