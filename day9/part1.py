f = open("input.txt", "r")
lines = f.readlines()

rows = len(lines)
cols = len(lines[0].strip())

mins = []
for i in range(rows):
    for j in range(cols):
        curr_item = int(lines[i][j])

        if i - 1 >= 0:
            item_above = int(lines[i - 1][j])
            if item_above <= curr_item:
                continue
        if i + 1 < rows:
            item_below = int(lines[i + 1][j])
            if item_below <= curr_item:
                continue
        if j - 1 >= 0:
            item_left = int(lines[i][j - 1])
            if item_left <= curr_item:
                continue
        if j + 1 < cols:
            item_right = int(lines[i][j + 1])
            if item_right <= curr_item:
                continue

        mins.append(curr_item)


print(sum([x + 1 for x in mins]))
