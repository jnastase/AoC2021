f = open("input.txt", "r")
lines = f.readlines()

readings = [int(x) for x in lines]

last_number = None
increases = 0
for reading in readings:
    deeper = False
    if last_number:
        deeper = reading > last_number

    if deeper:
        increases += 1
    last_number = reading

print(increases)
