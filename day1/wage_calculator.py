print("=" * 40)
print("WAGE CALCULATOR")
print("=" * 40)
print()

name = input("Workers name: ")
hours = float(input("Hours worked: "))
rate = float(input("Hourly rated: $"))

gross = hours * rate
tax = gross * 0.20
net = gross - tax

print()
print(f"Worker: {name}")
print(f"Hours: {hours}")
print(f"Rate: ${rate:.2f}/hour")
print()
print(f"Gross pay: ${gross:.2f}")
print(f"Tax (20%): ${tax:.2f}")
print(f"Net pay: ${net:.2f}")
