f = open("input.txt", "r")
lines = f.readlines()

total = 0
for line in lines:
    digits = line.split("|")[1].split()
    total += sum([1 if len(x) in [2, 3, 4, 7] else 0 for x in digits])


print(total)
