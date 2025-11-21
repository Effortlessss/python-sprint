def calculate_speed(lines, minutes):
    return lines / minutes
speed1 = calculate_speed (300, 60)
speed2 = calculate_speed (200, 20)
speed3 = calculate_speed (100, 10)
print(f"Speed: {speed1:.2f} lines/min")
print(f"Speed: {speed2:.2f} lines/min")
print(f"Speed: {speed3:.2f} lines/min")
