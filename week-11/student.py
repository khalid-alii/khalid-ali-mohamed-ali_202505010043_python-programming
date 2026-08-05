def get_student():
    print("===== Computer Lab Access =====")
    
    name = input("Student Name : ")
    student_id = input("Student ID : ")
    
    registered_input = input("Registered for today's lab? (Y/N): ").strip().upper()
    open_input = input("Is the lab open? (Y/N): ").strip().upper()
    available_input = input("Computer Available? (Y/N): ").strip().upper()
    
    is_registered = (registered_input == 'Y')
    is_open = (open_input == 'Y')
    is_available = (available_input == 'Y')
    
    return name, student_id, is_registered, is_open, is_available