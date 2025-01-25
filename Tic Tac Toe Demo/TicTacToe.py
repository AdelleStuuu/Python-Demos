# Using a list to represent the Tic-Tac-Toe board
pos = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def board():
    print("", pos[0], "|", pos[1], "|", pos[2])
    print("―――+―――+―――")
    print("", pos[3], "|", pos[4], "|", pos[5])
    print("―――+―――+―――")
    print("", pos[6], "|", pos[7], "|", pos[8])
    print("")

def playerX_input(): 
    while True:
        position = input("Player X, enter your position (1-9): ")
        if position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            index = int(position) - 1  # Convert to zero-based index
            if pos[index] == "-":
                pos[index] = "X"  # Set the position to "X"
                break
            else:
                print("Position already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def playerO_input(): 
    while True:
        position = input("Player O, enter your position (1-9): ")
        if position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            index = int(position) - 1  # Convert to zero-based index
            if pos[index] == "-":
                pos[index] = "O"  # Set the position to "O"
                break
            else:
                print("Position already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)               # Diagonal
    ]

    for combo in winning_combinations:
        if pos[combo[0]] == pos[combo[1]] == pos[combo[2]] and pos[combo[0]] != "-":
            print(f"Player {pos[combo[0]]} wins!")
            return True

    if "-" not in pos:
        print("It's a draw!")
        return True
    
    return False

def main():
    board()
    while True:
        playerX_input()
        board()
        if check_winner():
            break
        
        playerO_input()
        board()
        if check_winner():
            break

main()


