f = open("input.txt", "r")
lines = f.readlines()

rows = len(lines)
cols = len(lines[0].strip())

mins = []
for i in range(rows):
    for j in range(cols):
        curr_item = int(lines[i][j])

        pass


print(sum([x + 1 for x in mins]))
