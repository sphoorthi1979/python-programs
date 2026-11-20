# Step 1: Create an empty board
board = [" "] * 9


# Step 2: Display the board
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])


# Step 3: Check if a player has won
def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        a, b, c = combo

        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Step 4: Start with player X
player = "X"

# Step 5: Run the game
while True:

    print_board()

    # Ask the player for a position
    try:
        position = int(input(f"Player {player}, enter position (1-9): "))
    except ValueError:
        print("Please enter a number!")
        continue

    # Check whether position is valid
    if position < 1 or position > 9:
        print("Choose a number from 1 to 9!")
        continue

    # Check whether position is already taken
    if board[position - 1] != " ":
        print("Position already taken!")
        continue

    # Put player's symbol on the board
    board[position - 1] = player

    # Check for winner
    if check_winner(player):
        print_board()
        print("Player", player, "wins!")
        break

    # Check for draw
    if " " not in board:
        print_board()
        print("It's a draw!")
        break

    # Change player
    if player == "X":
        player = "O"
    else:
        player = "X"
