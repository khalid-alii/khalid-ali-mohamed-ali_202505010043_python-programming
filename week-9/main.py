import ticket
import display

def main():
    name, id, issue, location, priority = ticket.create_ticket()

    technician = " "  
    if priority.lower() == "High":
        technician = "Ahmed"
    elif priority.lower() == "Medium":
        technician = "Siti" 
    else:
        technician = "Ali"

    display.display_ticket(name, id, issue, location, priority, technician)

if __name__ == "__main__":
    main()