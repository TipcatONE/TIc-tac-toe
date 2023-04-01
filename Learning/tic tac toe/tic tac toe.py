def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- | - | -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- | - | -')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


test_board = [" "] * 10


def player_input():
    player_1 = input("choose the side X or O"'\n')
    answers = {"X", "x", "O", "o"}
    zero = {"O", "o"}
    while player_1 not in answers:
        player_1 = input("Please choose side"'\n')
    if player_1 not in zero:
        return "x"
    else:
        return "o"


def place_marker(board, position):
    if player_input() == "x":
        marker = "X"
    else:
        marker = "O"
    if marker.upper() == marker:
        board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # горизонталь сверху
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # горизонталь в середине
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # горизонталь снизу
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # вертикаль слева
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # вертикаль в середине
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # вертикаль справа
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # диагональ
            (board[9] == mark and board[5] == mark and board[1] == mark))  # диагональ


win_check(test_board, "X")

import random


def choose_first():
    a = random.randint(1, 2)
    if a == 1:
        return 1
    else:
        return 2


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    if " " not in board[1:10]:
        return True
    else:
        return False


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(test_board, position):
        position = int(input('choose 1-9'))

    return position


def replay():
    return input('Вы хотите сыграть снова? Yes или No: ').lower().startswith('y')


import time

print('Добро пожаловать в игру Крестики-Нолики!')
time.sleep(0.2)

while True:
    # Настройка игры
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('Первым ходит ' + turn + '.')

    play_game = input('Вы готовы играть? Введите Yes или No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок 1':
            # Ход Игрока 1

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Поздравляю! Вы выиграли!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 2'

        else:
            # Ход Игрока 2

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Игрок 2 выиграл!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 1'

    if not replay():
        break
