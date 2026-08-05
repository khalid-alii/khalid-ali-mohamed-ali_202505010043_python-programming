import customer
import receipt

def main():
    name, food, quantity, price, delivery_charges = customer.get_customer()
    
    receipt.print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()