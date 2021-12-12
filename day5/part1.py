f = open("input.txt", "r")
lines = f.readlines()

max_col_index = 999  # probably not right but shouldn't matter
points = {}
for line in lines:
    coords = line.split(" -> ")
    (x1, y1) = (int(x) for x in coords[0].split(","))
    (x2, y2) = (int(x) for x in coords[1].split(","))

    if x1 == x2:
        start = min(y1, y2)
        end = max(y1, y2)
        for i in range(start, end + 1):
            print(f"x: {i}")
            key = str((x1 * max_col_index) + i)
            points[key] = points.get(key, 0) + 1

    if y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2)
        for i in range(start, end + 1):
            print(f"y: {i}")
            key = str((i * max_col_index) + y1)
            points[key] = points.get(key, 0) + 1

total = sum([1 for k, v in points.items() if v > 1])

print(points)
print(total)
