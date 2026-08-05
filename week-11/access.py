def check_access(is_registered, is_open, is_available):
    if is_registered and is_open and is_available:
        return "Access Granted"
    else:
        return "Access Denied"

def get_reason(is_registered, is_open, is_available):
    if not is_registered:
        return "Student is not registered."
    elif not is_open:
        return "Computer lab is closed."
    elif not is_available:
        return "No available computer."
    else:
        return "Welcome to the lab."