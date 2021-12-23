f = open("input.txt", "r")
lines = f.readlines()


indices = set()


def handle_x(indices, index):
    below_fold = {(x, y) for (x, y) in indices if x > index}
    above_fold = {(x, y) for (x, y) in indices if x < index}
    for (x, y) in below_fold:
        new_x = index - (x - index)
        above_fold.add((new_x, y))

    return above_fold


def handle_y(indices, index):
    right_fold = {(x, y) for (x, y) in indices if y > index}
    left_fold = {(x, y) for (x, y) in indices if y < index}
    for (x, y) in right_fold:
        new_y = index - (y - index)
        left_fold.add((x, new_y))

    return left_fold


for line in lines:
    if line and "," in line:
        vals = line.split(",")
        indices.add((int(vals[0]), int(vals[1])))

    if line and "=" in line:
        vals = line.split("=")
        axis = vals[0][-1]
        point = int(vals[1])

        if axis == "x":
            indices = handle_x(indices, point)

        if axis == "y":
            indices = handle_y(indices, point)

        print(len(indices))


# print(len(indices))
