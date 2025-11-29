def extract_numbers(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
    
        
        lines = content.split("\n") # split file into list of lines
        # Extract lines number
        first_line = lines[0] # "Lines: 100"
        lines_num = first_line.split(": ")[1] # "100"

        # Extract minutes number
        second_line = lines[1] # "Minutes: 180"
        minutes_num = second_line.split(": ")[1] # "180"
        
        print(f"Lines: {lines_num}, Minutes: {minutes_num}") # print

    except FileNotFoundError:
        print("File not found")
    extract_numbers("session.txt")

def extract_and_validate(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()

        lines = content.split("\n")

        # Extract
        lines_num = lines[0].split(": ")[1]
        minutes_num = lines[1].split(": ")[1]

        # Convert to integers
        lines_int = int(lines_num)
        minutes_int = int(minutes_num)

        # Validate positive
        if lines_int < 0 or minutes_int < 0:
            return "Error: negative numbers not allowed"

        return f"Valid data: {lines_int} lines, {minutes_int} minutes"

    except FileNotFoundError:
        return "Error: File not found"
    except ValueError:
        return "Error: False value input"

print(extract_and_validate("session.txt"))
        

