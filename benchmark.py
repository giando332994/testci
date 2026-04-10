import time
import random

def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

start = time.time()
compute()
end = time.time()

execution_time = end - start

# simulate variability
execution_time += random.uniform(0, 0.1)

with open("result.txt", "w") as f:
    f.write(f"execution_time={execution_time}\n")

print(f"Execution time: {execution_time}")