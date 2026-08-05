# main.py
import utils

def main():
    customer_name = input("Customer name: ")
    
    coffee_qty = int(input("Coffee quantity: "))
    tea_qty = int(input("Tea quantity: "))
    sandwich_qty = int(input("Sandwich quantity: "))
    
    total_bill = utils.calculate_total(coffee_qty, tea_qty, sandwich_qty)
    
    utils.print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total_bill)

if __name__ == "__main__":
    main()