f = open("input.txt", "r")
lines = f.readlines()

positions = [int(x) for x in lines[0].split(",")]
max_value = max(positions)

lowest_index = None
lowest_total = None

for i in range(max_value):
    total = sum([abs(x - i) for x in positions])

    if not lowest_index or total < lowest_total:
        lowest_total = total
        lowest_index = i

print(lowest_index)
print(lowest_total)
