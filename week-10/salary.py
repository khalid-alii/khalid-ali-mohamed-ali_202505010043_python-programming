OVERTIME_RATE = 25.00
LOYALTY_BONUS_AMOUNT = 700.00

def calculate_gross(basic, allowance, overtime_hours, years_worked):
    """Calculates total gross salary including overtime and bonuses."""

    overtime_pay = overtime_hours * OVERTIME_RATE
    
    if years_worked > 3:
        bonus = LOYALTY_BONUS_AMOUNT
    else:
        bonus = 0.00
        
    total_gross = basic + allowance + overtime_pay + bonus
    
    return total_gross, overtime_pay, bonus

def calculate_epf(gross_salary):
    """Calculates EPF deduction (11% of gross)."""
    return gross_salary * 0.11

def calculate_socso(gross_salary):
    """Calculates SOCSO deduction (0.5% of gross)."""
    return gross_salary * 0.005

def calculate_net(gross_salary, epf, socso):
    """Calculates net salary after deductions."""
    return gross_salary - epf - socso