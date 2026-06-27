import math

# Display the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()

# Check winner
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Check draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Minimax Algorithm
def minimax(board, depth, is_max):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best = min(best, score)
        return best

# AI Move
def ai_move(board):
    best_score = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = "O"

# Human Move
def player_move(board):
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already occupied.")
            else:
                print("Invalid position.")
        except:
            print("Enter valid numbers.")

# Main Game
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("===== TIC TAC TOE AI =====")
    print("You are X")
    print("AI is O")

    while True:
        print_board(board)

        player_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("You Win!")
            break

        if is_draw(board):
            print_board(board)
            print("Match Draw!")
            break

        print("AI is thinking...")

        ai_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("AI Wins!")
            break

        if is_draw(board):
            print_board(board)
            print("Match Draw!")
            break

if __name__ == "__main__":
    main()