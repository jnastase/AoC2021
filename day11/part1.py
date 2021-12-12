f = open("input.txt", "r")
lines = f.readlines()

rows = len(lines)
cols = len(lines[0].strip())


def increment_grid():
    flashed_indices = {}
    for i in range(rows):
        for j in range(cols):
            next_val = int(lines[i][j]) + 1

            lines[i][j] = next_val

            if next_val > 9:
                flashed_indices.append((i * rows) + j)


for step in range(100):
    increment_grid()


print(sum([score_char(x) for x in illegal_chars]))
