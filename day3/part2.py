f = open("input.txt", "r")
lines = f.readlines()

bin_arrays = [list(x) for x in lines]

zipped_vals = zip(*bin_arrays)

oxygen_vals = [*lines]
co2_vals = [*lines]
curr_index = 0
for i in range(len(lines[0])):
    remaining_count = len(oxygen_vals)
    if remaining_count <= 1:
        break

    index_sum = sum([int(x[i]) for x in oxygen_vals])

    use_ones = index_sum >= remaining_count / 2
    oxygen_vals = [x for x in oxygen_vals if x[i] == ("1" if use_ones else "0")]
    curr_index += 1

for i in range(len(lines[0])):
    remaining_count = len(co2_vals)
    if remaining_count <= 1:
        break

    index_sum = sum([int(x[i]) for x in co2_vals])

    use_ones = index_sum < remaining_count / 2
    co2_vals = [x for x in co2_vals if x[i] == ("1" if use_ones else "0")]
    curr_index += 1


o = int(oxygen_vals[0], 2)
c = int(co2_vals[0], 2)

print(o * c)
