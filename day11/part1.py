f = open("input.txt", "r")
lines = f.readlines()

rows = len(lines)
cols = len(lines[0].strip())

grid = []
for line in lines:
    grid.append([int(x) for x in line.strip()])


def increment_grid():
    flashed_indices = []
    for i in range(rows):
        for j in range(cols):
            next_val = grid[i][j] + 1

            grid[i][j] = next_val

            if next_val > 9:
                flashed_indices.append((i, j))

    return flashed_indices


def handle_flashes(indices):
    flash_count = 0
    while indices:
        flash_count += 1
        x, y = indices.pop()

        top_left = (x - 1, y - 1) if x - 1 >= 0 and y - 1 >= 0 else None
        top = (x - 1, y) if x - 1 >= 0 else None
        top_right = (x - 1, y + 1) if x - 1 >= 0 and y + 1 < cols else None

        left = (x, y - 1) if y - 1 >= 0 else None
        right = (x, y + 1) if y + 1 < cols else None

        bottom_left = (x + 1, y - 1) if x + 1 < rows and y - 1 >= 0 else None
        bottom = (x + 1, y) if x + 1 < rows else None
        bottom_right = (x + 1, y + 1) if x + 1 < rows and y + 1 < cols else None

        if (
            top_left
            and grid[top_left[0]][top_left[1]]
            and grid[top_left[0]][top_left[1]] < 10
        ):
            grid[top_left[0]][top_left[1]] += 1
            if grid[top_left[0]][top_left[1]] == 10:
                indices.append(top_left)

        if top and grid[top[0]][top[1]] and grid[top[0]][top[1]] < 10:
            grid[top[0]][top[1]] += 1
            if grid[top[0]][top[1]] == 10:
                indices.append(top)

        if (
            top_right
            and grid[top_right[0]][top_right[1]]
            and grid[top_right[0]][top_right[1]] < 10
        ):
            grid[top_right[0]][top_right[1]] += 1
            if grid[top_right[0]][top_right[1]] == 10:
                indices.append(top_right)

        if left and grid[left[0]][left[1]] and grid[left[0]][left[1]] < 10:
            grid[left[0]][left[1]] += 1
            if grid[left[0]][left[1]] == 10:
                indices.append(left)

        if right and grid[right[0]][right[1]] and grid[right[0]][right[1]] < 10:
            grid[right[0]][right[1]] += 1
            if grid[right[0]][right[1]] == 10:
                indices.append(right)

        if (
            bottom_left
            and grid[bottom_left[0]][bottom_left[1]]
            and grid[bottom_left[0]][bottom_left[1]] < 10
        ):
            grid[bottom_left[0]][bottom_left[1]] += 1
            if grid[bottom_left[0]][bottom_left[1]] == 10:
                indices.append(bottom_left)

        if bottom and grid[bottom[0]][bottom[1]] and grid[bottom[0]][bottom[1]] < 10:
            grid[bottom[0]][bottom[1]] += 1
            if grid[bottom[0]][bottom[1]] == 10:
                indices.append(bottom)

        if (
            bottom_right
            and grid[bottom_right[0]][bottom_right[1]]
            and grid[bottom_right[0]][bottom_right[1]] < 10
        ):
            grid[bottom_right[0]][bottom_right[1]] += 1
            if grid[bottom_right[0]][bottom_right[1]] == 10:
                indices.append(bottom_right)

    return flash_count


def reset_flashed():
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 10:
                grid[i][j] = 0


total = 0
for step in range(100):
    indices = increment_grid()
    total += handle_flashes(indices)
    reset_flashed()

    if step < 10:
        print("**************************************")
        print(grid)


print(total)
