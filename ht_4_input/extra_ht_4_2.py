import random

n = int(input("Enter the n value: "))
x, y = 0, 0
steps = 0
while abs(x) < n and abs(y) < n:
    direction = random.choice("EWNS")
    if direction == "E":
        x += 1
    elif direction == "W":
        x -= 1
    elif direction == "N":
        y += 1
    elif direction == "S":
        y -= 1
    steps += 1

print(f"It will take {steps} steps to hit the boundary")
