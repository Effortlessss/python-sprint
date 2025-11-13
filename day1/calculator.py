num1 = int(input("First number: "))
num2 = int(input("Second number: "))

result = num1 + num2

print(f"Result: {result}")


bill = float(input("Bill amount: $"))
percent = float(input("Tip percent: "))
print()
tip = bill * (percent / 100)
total = bill + tip
print()
print(f"Bill: ${bill:.2f}")
print(f"Tip ({percent}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
