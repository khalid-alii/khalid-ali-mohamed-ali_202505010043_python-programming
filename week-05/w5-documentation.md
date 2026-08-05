# Week 5 Documentation

## 1. Problem Analysis

**1.1 Define the problem statement:**
* Build a system for a small cafe to calculate their bills, insteade of doing manually.

**1.2 What are the Inputs?**
* Customer Name 
* Quantity of Coffee 
* Quantity of Tea 
* Quantity of Sandwich 

**1.3 What are the outputs?**
* A receipt showing the customer's name, the quantity of each item ordered, and the calculated total bill amount (in RM).

**1.4 What would be the typical process flow?**
1.  Ask the user to enter the Customer's Name.
2.  Ask for the quantities of items ordered.
3.  The program calculates the total cost.
4.  Print the recipt.

**1.5 What are the constraints?**
* The main constrain in this program is you can't change the orders after it's submitted.

## 2. Problem Decomposition
* We can cut this problem into 3 smaller problems:
1. Gathering the inputs from the coustemer (name, and orders)
2. Calculating the total of the orders.
3. Printing the recipte.

## 3. Pseudocode
START

// Define the prices
coffeePrice = 8.50
teaPrice = 6.00
sandwichPrice = 12.00

// Main Program Execution
print "Customer name: "
input customer_name
print "Coffee quantity: "
input coffee_qty
print "Tea quantity: "
input tea_qty
print "Sandwich quantity: "
input sandwich_qty

total_bill = calculate_total(coffee_qty, tea_qty, sandwich_qty)

CALL print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total_bill)

END