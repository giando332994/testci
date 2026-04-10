with open("result.txt") as f:
    line = f.read()

time_value = float(line.split("=")[1])

if time_value > 0.5:
    print("WARNING: Performance degraded")
else:
    print("Performance OK")