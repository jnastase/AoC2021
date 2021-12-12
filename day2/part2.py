f = open("input.txt", "r")
lines = f.readlines()

horizontal = 0
depth = 0
aim = 0
for line in lines:
    vals = line.split()
    op = vals[0]

    if op == "up":
        aim -= int(vals[1])
    elif op == "down":
        aim += int(vals[1])
    elif op == "forward":
        horizontal += int(vals[1])
        depth += aim * int(vals[1])

print(horizontal * depth)
