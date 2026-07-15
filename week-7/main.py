from food_order import calculate_total

def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))

        total = calculate_total(price, quantity)

        if isinstance(total, str):
            print(f"Error: {total}")
        else:
            print(f"Total Payment = RM {total:.2f}")
            
    except ValueError:
        print("Error: Invalid input format. Please enter numerical values.")

if __name__ == "__main__":
    main()