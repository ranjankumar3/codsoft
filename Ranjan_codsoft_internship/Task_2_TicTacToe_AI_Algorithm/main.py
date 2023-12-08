import random

# print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# check if the game is a draw
def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# AI's move using Minimax algorithm
def ai_move(board, depth, is_maximizer):
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if check_draw(board):
        return 0

    if is_maximizer:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = ai_move(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = ai_move(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# the AI's move implemenation
def make_ai_move(board):
    best_move = None
    best_score = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = ai_move(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

# Function to play the Tic-Tac-Toe game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter your move (row and column, e.g., '1 1'): ").split())
        if board[row - 1][col - 1] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row - 1][col - 1] = 'X'
        print_board(board)

        # Checking if player wins
        if check_win(board, 'X'):
            print("You win!")
            break

        # Checking if it's a draw
        if check_draw(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is making its move...")
        make_ai_move(board)
        print_board(board)

        # Checking if AI wins
        if check_win(board, 'O'):
            print("AI wins!")
            break

        # Check if it's a draw
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
