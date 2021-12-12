f = open("input.txt", "r")
lines = f.readlines()

horizontal = 0
depth = 0
for line in lines:
    vals = line.split()
    op = vals[0]

    if op == "up":
        depth -= int(vals[1])
    elif op == "down":
        depth += int(vals[1])
    elif op == "forward":
        horizontal += int(vals[1])

print(horizontal * depth)
