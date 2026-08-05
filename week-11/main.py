import student
import access
import display

def main():
    name, student_id, is_registered, is_open, is_available = student.get_student()
    
    status = access.check_access(is_registered, is_open, is_available)
    reason = access.get_reason(is_registered, is_open, is_available)
    
    display.print_result(name, student_id, status, reason)

if __name__ == "__main__":
    main()