f = open("input.txt", "r")
lines = f.readlines()

bin_arrays = [list(x) for x in lines]

zipped_vals = zip(*bin_arrays)

gamma_string = ""
epsilon_string = ""
for z in zipped_vals:
    val = sum(int(x) for x in z)
    if val > (len(z) / 2):
        gamma_string += "1"
        epsilon_string += "0"
    else:
        gamma_string += "0"
        epsilon_string += "1"

gamma = int(gamma_string, 2)
epsilon = int(epsilon_string, 2)
print(gamma_string)
print(gamma)

print(epsilon_string)
print(epsilon)

print(gamma * epsilon)
