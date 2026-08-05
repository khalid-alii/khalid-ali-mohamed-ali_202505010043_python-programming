# employee.py

def get_employee():
    print("=== Employee Information ===")
    
    # Declare and collect employee variables
    name = input("Employee Name : ")
    employee_id = input("Employee ID : ")
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))
    
    # Variables added for Inquiry 2.1 and 2.2
    overtime_hours = float(input("Overtime Hours : "))
    years_worked = int(input("Years Worked : "))
    
    # Return employee variables as a tuple
    return name, employee_id, basic_salary, allowance, overtime_hours, years_worked