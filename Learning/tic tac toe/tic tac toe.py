def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- | - | -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- | - | -')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n' * 100)


display_board(['#', 'X', 'o', 'X', 'o', 'x', 'o', 'x', 'o', '×'])


def player_input():
    player_1 = int(input("Print 1 if you wanna play x and 0 for play 0"'\n'"player 1 ="))
    if player_1 != 1 or player_1 != 0:
        print("Please write the number for choose side")
    elif player_1 == 1:
        return 1
    else:
        return 2
    if player_1 == 1:
        player_2 = 2
    elif player_1 == 0:
        player_2 = 1


player_input()
