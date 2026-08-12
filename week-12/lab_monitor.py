def check_computers():
    computers = [] # initial value
    
    # iterate & check for 5 computer
    for i in range(1, 6):
        # prompt the user to classify each computer to either
        # A - Available, U - Used, M - Maintenance
        # Using .upper() to ensure the input matches the capital "A" check later
        status = input(f"Computer {i} Status (A/U/M): ").upper() 
        computers.append(status)
        
    return computers

def count_available(computers):
    available = 0 # initial value
    
    for status in computers:
        if status == "A":
            available += 1
            
    return available

def display_status(computers, available):
    print("\n========== LAB STATUS ==========")
    
    for number in range(len(computers)):
        print(f"Computer {number + 1}: {computers[number]}")
        
    print("------------------------")
    print(f"Available Computers: {available}")
    print("================================")