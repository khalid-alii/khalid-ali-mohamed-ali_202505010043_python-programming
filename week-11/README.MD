# Week 11 - Computer Lab Access System

## Overview
City University has implemented a Computer Lab Access System to automate student entry into computer laboratories. This Python project uses industry-standard modular programming practices to verify entry conditions and grant or deny access accordingly.

## Conditions for Entry
Before a student is allowed to enter the lab, the system verifies three conditions:
1. Is the student registered for today's lab session?
2. Is the computer laboratory currently open?
3. Are there any computers available?

*Note: Only students who satisfy **all** conditions are allowed to enter.*

## Project Structure
The system is separated into multiple Python modules to improve software quality and maintainability:
* `main.py` - The main script that integrates all modules and runs the application.
* `student.py` - Handles user input for student details and lab conditions.
* `access.py` - Contains the logical operators and conditional statements to determine access status and reasons.
* `display.py` - Formats and prints the final access report to the console.
