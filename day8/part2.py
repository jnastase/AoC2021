f = open("input.txt", "r")
lines = f.readlines()

total = 0
for line in lines:
    digits = line.split("|")[0].split()
    display = line.split("|")[1].split()

    one = [x for x in digits if len(x) == 2][0]
    seven = [x for x in digits if len(x) == 3][0]
    four = [x for x in digits if len(x) == 4][0]
    eight = [x for x in digits if len(x) == 7][0]
    three = [
        x
        for x in digits
        if len(x) == 5 and all([True if y in x else False for y in one])
    ][0]

    display_string = ""
    for d in display:
        if len(d) == 2:
            display_string += "1"
        elif len(d) == 3:
            display_string += "7"
        elif len(d) == 4:
            display_string += "4"
        elif len(d) == 7:
            display_string += "8"
        elif len(d) == 5:
            if all([True if x in d else False for x in one]):
                display_string += "3"
            elif sum([1 if x in d else 0 for x in four]) == 3:
                display_string += "5"
            else:
                display_string += "2"
        elif len(d) == 6:
            if all([True if x in d else False for x in three]):
                display_string += "9"
            elif sum([1 if x in d else 0 for x in seven]) == 3:
                display_string += "0"
            else:
                display_string += "6"

    print(int(display_string))
    total += int(display_string)


print(total)
# 1138244
