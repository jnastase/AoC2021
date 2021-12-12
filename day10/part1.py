f = open("input.txt", "r")
lines = f.readlines()


def score_char(char):
    if char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == "}":
        return 1197
    elif char == ">":
        return 25137


illegal_chars = []
for line in lines:
    stack = []
    for char in line:
        if char in ["(", "{", "[", "<"]:
            stack.append(char)

        if char in [")", "}", "]", ">"]:
            val = stack.pop()
            if (
                (char == ")" and val != "(")
                or (char == "}" and val != "{")
                or (char == "]" and val != "[")
                or (char == ">" and val != "<")
            ):
                illegal_chars.append(char)
                break


print(sum([score_char(x) for x in illegal_chars]))
