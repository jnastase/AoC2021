f = open("input.txt", "r")
lines = f.readlines()

fishes = [int(x) for x in lines[0].split(",")]

day_0 = 0
day_1 = 0
day_2 = 0
day_3 = 0
day_4 = 0
day_5 = 0
day_6 = 0
day_7 = 0
day_8 = 0

for fish in fishes:
    if fish == 1:
        day_1 += 1
    elif fish == 2:
        day_2 += 1
    elif fish == 3:
        day_3 += 1
    elif fish == 4:
        day_4 += 1
    elif fish == 5:
        day_5 += 1
    elif fish == 6:
        day_6 += 1

results = {}
total = 0
for i in range(256):
    fish_to_add = day_0

    day_0 = day_1
    day_1 = day_2
    day_2 = day_3
    day_3 = day_4
    day_4 = day_5
    day_5 = day_6
    day_6 = day_7 + fish_to_add
    day_7 = day_8

    day_8 = fish_to_add

print(day_0 + day_1 + day_2 + day_3 + day_4 + day_5 + day_6 + day_7 + day_8)
