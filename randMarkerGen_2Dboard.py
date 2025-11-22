import random

def create_board():
    """Creates a 5x5 board filled with underscores."""
    return [['_' for _ in range(5)] for _ in range(5)]

def place_diamonds(board):
    """Randomly places 15 diamonds on the board."""
    positions = []
    for r in range(5):
        for c in range(5):
            positions.append((r, c))

    diamond_positions = random.sample(positions, 15)

    for r, c in diamond_positions:
        board[r][c] = 'X'

def print_board(board):
    """Prints the board to the console."""
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    board = create_board()
    place_diamonds(board)
    print_board(board)
