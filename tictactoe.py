# Function print the board
def print_board(moves: list) -> None:
    print(f'   |   |   \n {moves[0]} | {moves[1]} | {moves[2]} \n   |   |   ')
    print(f'-----------')
    print(f'   |   |   \n {moves[3]} | {moves[4]} | {moves[5]} \n   |   |   ')
    print(f'-----------')
    print(f'   |   |   \n {moves[6]} | {moves[7]} | {moves[8]} \n   |   |   ')


# Function to record player moves
def player_move(moves: list, counter: int) -> list:
    if counter % 2 == 0:
        index = "FALSE"
        while not index.isdigit():
            index = input("Where would Player 1 like to mark X (1-9): ")
            if int(index) > 9 or int(index) <= 0:
                print("That number is out of range!")
                index = "FALSE"
                continue
            if moves[int(index) - 1] == "O" or moves[int(index) - 1] == "X":
                index = "FALSE"
                print("That spot is taken!")
                continue
        index = int(index)
        moves[index - 1] = "X"
        return moves
    else:
        index = "FALSE"
        while not index.isdigit():
            index = input("Where would Player 2 like to mark O (1-9): ")
            if int(index) > 9 or int(index) <= 0:
                print("That number is out of range!")
                index = "FALSE"
                continue
            if moves[int(index) - 1] == "O" or moves[int(index) - 1] == "X":
                index = "FALSE"
                print("That spot is taken!")
                continue
        index = int(index)
        moves[index - 1] = "O"
        return moves


# Function to see if player wants to continue playing
def play() -> bool:
    user_input = input("Would you like to play again (Y or N)? ")
    if user_input.upper() == "Y":
        return True
    else:
        return False


# Function to see if a winner is found
def is_winner(moves: list) -> bool:
    if (moves[0] == "X" and moves[1] == "X" and moves[2] == "X") or (
            moves[3] == "X" and moves[4] == "X" and moves[5] == "X") or (
            moves[6] == "X" and moves[7] == "X" and moves[8] == "X"):
        print("Player 1 has won!")
        return True
    elif (moves[0] == "X" and moves[3] == "X" and moves[6] == "X") or (
            moves[1] == "X" and moves[4] == "X" and moves[7] == "X") or (
            moves[2] == "X" and moves[5] == "X" and moves[8] == "X"):
        print("Player 1 has won!")
        return True
    elif (moves[0] == "X" and moves[4] == "X" and moves[8] == "X") or (
            moves[2] == "X" and moves[4] == "X" and moves[6] == "X") or (
            moves[6] == "X" and moves[7] == "X" and moves[8] == "X"):
        print("Player 1 has won!")
        return True
    elif (moves[0] == "O" and moves[1] == "O" and moves[2] == "O") or (
            moves[3] == "O" and moves[4] == "O" and moves[5] == "O") or (
            moves[6] == "O" and moves[7] == "O" and moves[8] == "O"):
        print("PlaOer 2 has won!")
        return True
    elif (moves[0] == "O" and moves[3] == "O" and moves[6] == "O") or (
            moves[1] == "O" and moves[4] == "O" and moves[7] == "O") or (
            moves[2] == "O" and moves[5] == "O" and moves[8] == "O"):
        print("PlaOer 2 has won!")
        return True
    elif (moves[0] == "O" and moves[4] == "O" and moves[8] == "O") or (
            moves[2] == "O" and moves[4] == "O" and moves[6] == "O") or (
            moves[6] == "O" and moves[7] == "O" and moves[8] == "O"):
        print("Player 2 has won!")
        return True
    else:
        return False


# MAIN PROGRAM
curr_moves = [" ",  " ", " ", " ", " ", " ", " ", " ", " "]
count = 0
play_again = True
while play_again:
    while not is_winner(curr_moves):
        print('Here is the current board: ')
        print_board(curr_moves)
        player_move(curr_moves, count)
        count += 1
        continue
    print_board(curr_moves)
    play_again = play()
    curr_moves = [" ",  " ", " ", " ", " ", " ", " ", " ", " "]
    count = 0
print("Thanks for playing!")
