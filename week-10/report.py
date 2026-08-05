def print_report(name, employee_id, basic, allowance, ot_pay, bonus, gross, epf, socso, net):
    print(f"\n========== SALARY REPORT ==========")
    print(f"Employee Name : {name}")
    print(f"Employee ID   : {employee_id}")
    print("-" * 35)
    
    print(f"Basic Salary  : RM {basic:.2f}")
    print(f"Allowance     : RM {allowance:.2f}")
    if ot_pay > 0:
        print(f"Overtime Pay  : RM {ot_pay:.2f}")
    if bonus > 0:
        print(f"Loyalty Bonus : RM {bonus:.2f}")
        
    print("-" * 35)
    print(f"Gross Salary  : RM {gross:.2f}")
    print(f"EPF (11%)     : RM {epf:.2f}")
    print(f"SOCSO (0.5%)  : RM {socso:.2f}")
    print("-" * 35)
    print(f"Net Salary    : RM {net:.2f}")
    print("===================================")