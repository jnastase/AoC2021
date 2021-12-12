f = open("input.txt", "r")
lines = f.readlines()

numbers_to_call = [int(x) for x in lines[0].split(",")]
boards = []

next_board = []
for line in lines[1:]:
    if not line.strip():
        if next_board:
            boards.append(next_board)
        next_board = []
        continue

    next_board.append([x for x in line.split()])


def mark_board(board, last_num_called):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if int(board[i][j]) == last_num_called:
                board[i][j] = int(board[i][j])
                return True

    return False


def is_winner(board):
    for i in range(len(board[0])):
        if all([type(x) == int for x in board[i]]):
            return True

        if all([type(board[x][i]) == int for x in range(len(board[0]))]):
            print("cols")
            return True

    return False


def calc_score(board):
    total = 0
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if type(board[i][j]) == str:
                total += int(board[i][j])

    return total


last_num_called = None
winning_board = None
for n in numbers_to_call:
    for board in boards:
        if is_winner(board):
            continue

        has_num = mark_board(board, n)
        if has_num:
            did_win = is_winner(board)
            if did_win:
                winning_board = board
                last_num_called = n
                print("win")


score = calc_score(winning_board)
print(score * last_num_called)
print(last_num_called)
