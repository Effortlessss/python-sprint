def add_applications(company, position, date, status):
    with open("applications.txt", "a") as f:
        f.write(f"{company} | {position} | {date} | {status}\n")

# Test it
add_applications("RemoteHQ", "VA", "2025-11-26", "Applied")
print("Application saved")

def view_applications():
    try:
        with open("applications.txt", "r") as f:
            lines = f.readlines()

            print("YOUR JOB APPLICATIONS:")
            print("-" * 50)
            
            for line in lines:
                parts = line.strip().split(" | ")
                print(f"Company: {parts[0]}")
                print(f"Position: {parts[1]}")
                print(f"Date {parts[2]}")
                print(f"Status: {parts[3]}")
                print("-" * 50)
    except FileNotFoundError:
        print("No pplications saved yet")

view_applications()


