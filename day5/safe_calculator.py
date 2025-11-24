def safe_divisions(a, b):
    try:
        result = a / b
        return result 
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input types"
    
# Test cases
print(safe_divisions(10, 20))  # Normal
print(safe_divisions(69, 0))   # Division by 0
print(safe_divisions("h", 5))  # An invalid input type

# Chall 3 

def tracked_divide(a, b):
    try:
        result = a / b
        print(f"Success: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Divisions by zero")
        return None
    except TypeError:
        print("Error: Incorect input type")
        return None
    finally:
        print("Calculation complete")

tracked_divide(4, 2) # Correct
print()
tracked_divide(4, 0) # Zero
print()
tracked_divide("h", 5) # Incorrect input
        


