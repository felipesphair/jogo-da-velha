import random


def display_board(board):
   
    print('    |   |    ')
    print('  '+board[7]+' | '+board[8]+' | '+board[9])
    print('    |   |    ')
    print('--------------')
    print('    |   |    ')
    print('  '+board[4]+' | '+board[5]+' | '+board[6])
    print('    |   |    ')
    print('--------------')
    print('    |   |    ')
    print('  '+board[1]+' | '+board[2]+' | '+board[3])
    print('    |   |    ')

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Você quer ser X ou O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker
      

def win_check(board, mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2 começa!'
    else:
        return 'Player 1 começa!'

def space_check(board, position):
    if (board[position] != 'X' and board[position] != 'O'):
        return True
    else:
        return False

def full_board_check(board):
    for i in board:
        if i not in ['X','O']:
            return False
    return True

def player_choice(board):
    position = ' '
    while (position not in '1 2 3 4 5 6 7 8 9'.split()) or not (space_check(board, int(position))):
        position = input('Escolha sua jogada (1-9): ')

        if position in '1 2 3 4 5 6 7 8 9'.split() and not space_check(board, int(position)):
            print('Essa posição já está marcada. Escolha outra posição.')
    return int(position)

def replay():
    return input('Quer jogar novamente? "SIM" ou "NÃO": ').lower().strip().startswith('s')

while True:
    
    print('BEM VINDO AO JOGO DA VELHA!')
    board = ['X','1','2','3','4','5','6','7','8','9']
    player1_marker, player2_marker = player_input()
    turn = choose_first()

    game_on = True

    while game_on:
        if turn == 'Player 1 começa!':
            print('Vez do Player 1!')
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Parabéns! Você venceu!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print('Empate!')
                game_on = False
            else:
                turn = 'Player 2 começa!'
        else:
            display_board(board)
            print('Vez do Player 2!')
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Parabéns! Você venceu!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print('Empate!')
                game_on = False
            else:
                turn = 'Player 1 começa!'

    if not replay():
        break
