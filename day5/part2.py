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
            key = str((x1 * max_col_index) + i)
            points[key] = points.get(key, 0) + 1
    elif y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2)
        for i in range(start, end + 1):
            key = str((i * max_col_index) + y1)
            points[key] = points.get(key, 0) + 1
    else:
        up = False
        if x1 < x2 and y2 < y1 or x2 < x1 and y1 < y2:
            up = True

        if up:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            y = max(y1, y2)
            for i in range(min_x, max_x + 1):
                key = str((i * max_col_index) + y)
                points[key] = points.get(key, 0) + 1
                y -= 1
        else:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            y = min(y1, y2)
            for i in range(min_x, max_x + 1):
                key = str((i * max_col_index) + y)
                points[key] = points.get(key, 0) + 1
                y += 1


total = sum([1 for k, v in points.items() if v > 1])

print(points)
print(total)
