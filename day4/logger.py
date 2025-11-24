# Function1: save data
def save_session(lines, minutes, filename):
    speed = lines / minutes
    with open(filename, "a") as f:
        f.write(f"Lines: {lines}\n")
        f.write(f"Minutes: {minutes}\n")
        f.write(f"Speed: {speed:.2f} lines/min\n")
save_session(100, 180, "session.txt")
print("Session saved to session.txt")
#Function2: read data
def load_session(filename):
    with open(filename, "r") as f:
        content = f.read()
        print(content)
#Call function1 
save_session(247, 420, "session.txt")
print("Session saved")
#Call function2
load_session("session.txt")

    
