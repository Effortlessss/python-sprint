def analyze_session(lines, minutes):
    speed = lines / minutes
    hours = minutes / 60
    lines_per_hour = lines / hours
    #new
    minutes_per_line = minutes/lines
    return speed, lines_per_hour, minutes_per_line

speed, hourly, min_per_line = analyze_session(100, 180)
print(f"Speed: {speed:.2f}/min, {hourly:.2f}/hour")
print(f"Hourly: {hourly:.2f}/hour")
print(f"Minutes per line: {min_per_line:.2f} min/line")

def productivity_rate(lines_per_minute):
    if lines_per_minute == 0: 
        return "UR TOO SLOW!!!"
    elif lines_per_minute > 1:
        return "UR A CODE GOD!!!"
    elif lines_per_minute >= 0.5:
        return "AVERAGE..."
    else:
        return "UR TOO SLOW!!!"
rating = productivity_rate(0.56)
print(f"Productivity Rating: {rating}")    
