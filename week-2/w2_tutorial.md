# Check Chack
A program that checks if users are eligible to enter the movies theater.

## 1. The Components
### 1.1 The Inputs
- User's age.
- Companion's age.
- User's ticket.
- Companion's ticket.
### 1.2 The Process
- User enters the required info (age, ticket, companion's age...).
- The program checks it.
- The program output if the user is eligible to enter the theater or not.
### The Output
- A QR to enter the theater if the user is eligible.
- " Sorry you are not eligible to enter the theater" if the user is not eligible.

## 2. The Algorithm
### 2.1 The Diagram
![alt text](<Check Chack.drawio (1).png>)
### 2.2 Truth Table

| User 13 or older | User has a ticket | User with companion | Companion has a ticket | Can enter | Can't enter |
| :--- | :---: | ---: | ---: | ---: | ---: |
| True | True | False | False | True | False |
| False | True | True | True | True | False |
### 2.3 Algorithm
- User enters his age.
- If he's 13 or older enters his ticket and give him the QR.
- If not check if he has an adult companion with a ticket then give him the QR.
- If not print the appology message.
### 2.4 Peseudocode
START
    // Step 1: Initialize Variables (Inputs)
    DECLARE age AS Integer
    DECLARE accompanied_by_adult AS Boolean
    DECLARE has_valid_ticket AS Boolean

    // Step 2: Retrieve User Inputs
    PRINT "Enter the user's age:"
    READ age
    
    PRINT "Is the user accompanied by an adult? (True/False):"
    READ accompanied_by_adult
    
    PRINT "Does the user have a valid ticket? (True/False):"
    READ has_valid_ticket

    // Step 3: Evaluate Admission Logic (Process & Output)
    IF has_valid_ticket == True THEN
        
        IF age >= 13 OR accompanied_by_adult == True THEN
            PRINT "Admission Granted: The user is allowed to enter."
        ELSE
            PRINT "Admission Denied: The user is under 13 and not accompanied by an adult."
        END IF
        
    ELSE
        PRINT "Admission Denied: The user does not have a valid ticket."
    END IF
END