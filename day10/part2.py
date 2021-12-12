f = open("input.txt", "r")
lines = f.readlines()


def score_char(char):
    if char == ")":
        return 1
    elif char == "]":
        return 2
    elif char == "}":
        return 3
    elif char == ">":
        return 4


total_scores = []
for line in lines:
    is_valid = True
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
                is_valid = False
                break

    score = 0
    if is_valid:
        complete_char = []
        while len(stack):
            val = stack.pop()
            if val == "(":
                complete_char.append(")")
            elif val == "{":
                complete_char.append("}")
            elif val == "[":
                complete_char.append("]")
            elif val == "<":
                complete_char.append(">")

        score = 0
        for val in complete_char:
            score = score * 5
            score += score_char(val)

        total_scores.append(score)

total_scores.sort()
print(total_scores[len(total_scores) // 2])
