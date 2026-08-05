# Week 10 - Employee Salary Calculator

## Overview
Developed as a solution for an HR software company transitioning from manual calculation to an automated system. This Python project functions as a simple modular salary calculator.

## Features
* **Modular Design:** Code logic is separated into specific workflows (`main.py`, `employee.py`, `salary.py`, `report.py`) for better organization.
* **Basic Calculations:** Computes Gross Salary based on Basic Pay and Allowances, and calculates Net Salary after standard deductions.
* **Standard Deductions:** Automatically calculates EPF (11%) and SOCSO (0.5%).
* **Overtime Integration:** Automatically calculates overtime pay at a rate of RM 25.00/hour.
* **Loyalty Reward:** Recognizes employees who have worked for more than 3 years and automatically awards a loyalty bonus (Default: RM 500.00).

## Project Structure
* `main.py` - Coordinates the workflow and executes the program.
* `employee.py` - Manages user prompts to collect employee data.
* `salary.py` - Contains the mathematical functions for earnings and deductions.
* `report.py` - Prints the finalized salary slip to the console.