f = open("input.txt", "r")
lines = f.readlines()

fish = [int(x) for x in lines[0].split(",")]

for i in range(80):
    fish_to_add = [8 for x in fish if x == 0]
    fish = [x - 1 if x != 0 else 6 for x in fish]
    if fish_to_add:
        fish.extend(fish_to_add)

print(len(fish))
