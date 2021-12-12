f = open("input.txt", "r")
lines = f.readlines()

readings = [int(x) for x in lines]
print(readings[0:3])
groupings = []
for i in range(3, len(readings) + 1):
    print(sum(readings[i - 3 : i]))
    groupings.append(sum(readings[i - 3 : i]))


last_number = None
increases = 0
curr_group_counter = 0
for reading in groupings:
    deeper = False
    if last_number:
        deeper = reading > last_number

    if deeper:
        increases += 1
    last_number = reading

print(increases)
