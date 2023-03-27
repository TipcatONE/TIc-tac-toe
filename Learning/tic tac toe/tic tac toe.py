def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- | - | -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- | - | -')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n' * 100)


display_board(['#', 'X', 'o', 'X', 'o', 'x', 'o', 'x', 'o', '×'])


def player_input():
    player_1 = input("p1 == ")
    if player_1 != "x":
        return
    else:
        return False


player_input()


def proverka():
    map(player_input(), proverka())
