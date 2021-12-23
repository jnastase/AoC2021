f = open("input.txt", "r")
lines = f.readlines()

starting_string = ""
rules = {}

for line in lines:
    if line and not starting_string:
        starting_string = line.strip()
        continue

    if line and ">" in line:
        rule = line.split(" -> ")
        rules[rule[0]] = rule[1].strip()


for step in range(10):
    new_val = ""
    for i in range(len(starting_string) - 1):
        j = i + 1
        m = rules[f"{starting_string[i]}{starting_string[j]}"]
        if i == 0:
            new_val += f"{starting_string[i]}{m}{starting_string[j]}"
        else:
            new_val += f"{m}{starting_string[j]}"

    starting_string = new_val
    # print(starting_string)

char_dict = {}
for c in starting_string:
    if c in char_dict.keys():
        char_dict[c] += 1
    else:
        char_dict[c] = 1

high = max([x for x in char_dict.values()])
low = min([x for x in char_dict.values()])

print(high)
print(low)
print(high - low)
