def create_ticket():
    print("=== IT DESKHELP TICKET ===")
    name = input("Student Name: ")
    id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")
    priority = input("Priority (High/Medium/Low): ")
    return name, id, issue, location, priority