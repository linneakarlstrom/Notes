# Create a board
# Show the board
# play the game
# switch the turn between computer and person
# Check if win
 # - Check the columns
 # - check the rows
 # - check the diagonals
# check if tie

board_structure = [
    "-", "-", "-", "-", "-", "-"
    "-", "-", "-", "-", "-", "-"
    "-", "-", "-", "-", "-", "-"
    "-", "-", "-", "-", "-", "-"
    "-", "-", "-", "-", "-", "-"
    "-", "-", "-", "-", "-", "-"
]
def show_board():
    print(board_structure[0] + "|" + board_structure[1] +  "|" + board_structure[2] + "|" + board_structure[3] + "|" + board_structure[4] + "|" + board_structure[5] )
    print(board_structure[6] + "|" + board_structure[7] +  "|" + board_structure[8] + "|" + board_structure[9] + "|" + board_structure[10] + "|" + board_structure[11])
    print(board_structure[12] + "|" + board_structure[13] +  "|" + board_structure[14] + "|" + board_structure[15] + "|" + board_structure[16]+ "|" + board_structure[17])
    print(board_structure[18] + "|" + board_structure[19] +  "|" + board_structure[20] + "|" + board_structure[21] + "|" + board_structure[22] + "|" + board_structure[23])
    print(board_structure[24] + "|" + board_structure[25] +  "|" + board_structure[26] + "|" + board_structure[27] + "|" + board_structure[28] + "|" + board_structure[29])

show_board()
