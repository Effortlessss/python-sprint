def load_session(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: {filename} not found")


load_session("nonexistent.txt")

load_session("session.txt")