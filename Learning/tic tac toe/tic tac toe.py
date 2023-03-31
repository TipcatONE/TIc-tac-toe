def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- | - | -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- | - | -')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


test_board = [" "] * 10
display_board(test_board)


def player_input():
    player_1 = input("choose the side X or O"'\n')
    answers = {"X", "x", "O", "o"}
    zero = {"O", "o"}
    while player_1 not in answers:
        player_1 = input("Please choose side"'\n')
        print(player_1)
    if player_1 not in zero:
        return "x"
    else:
        return "o"


def place_marker(board):
    if player_input() == "x":
        marker = "X"
    else:
        marker = "O"
    position = int(input("Position ------"))
    if marker.upper() == marker:
        board[position] = marker


place_marker(test_board)
display_board(test_board)
place_marker(test_board)
display_board(test_board)
place_marker(test_board)
display_board(test_board)
place_marker(test_board)
display_board(test_board)
