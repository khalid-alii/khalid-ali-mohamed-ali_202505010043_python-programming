import lab_monitor

def main():
    while True:
        computers = lab_monitor.check_computers()
        available = lab_monitor.count_available(computers)
        lab_monitor.display_status(computers,  available)
        
        
        repeat = input("\nPerform another monitoring cycle? (Y/N): ").upper()
        if repeat != 'Y':
            break

if __name__ == "__main__":
    main()