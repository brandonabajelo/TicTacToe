import random

def display_board(board):
    #clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('____________________________________________________________________')

def player_input():
    marker = ''
    while not (marker == 'x' or marker == 'o'):
        marker = raw_input("Player 1: Select 'x' or 'o' as your marker! \n").lower()

    if marker == 'x':
        return ('x', 'o')
    else:
        return ('o', 'x')

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #top row

        (board[4] == mark and board[5] == mark and board[6] == mark) or # middle row

        (board[1] == mark and board[2] == mark and board[3] == mark) or # bottom row

        (board[7] == mark and board[4] == mark and board[1] == mark) or # left column

        (board[8] == mark and board[5] == mark and board[2] == mark) or # middle column

        (board[9] == mark and board[6] == mark and board[3] == mark) or # right column

        (board[1] == mark and board[5] == mark and board[9] == mark) or # diagonol

        (board[7] == mark and board[5] == mark and board[3] == mark)) # diagonol

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next move (1-9)\n')
        display_board(board)

    return int(position)

def replay():
    answer = ''
    while answer not in 'y n'.split():
        answer = raw_input('Do you want to play again? Y or N \n')

    answer = (True if answer == 'y' else False)
    return answer
    '''
    if answer == 'y':
        return True
    else:
        return False
    '''

def goodbye():
    print("Thanks for playing")

                    ###start game###

print("Welcome to the Tic Tac Toe game!")

while True:
    # reset the board
    gameBoard = [' '] *10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")
    game_on = True

    while game_on:

        if turn == "Player 1":

            display_board(gameBoard)

            playerOneMove = player_choice(gameBoard)

            place_marker(gameBoard, player1_marker, playerOneMove)
            display_board(gameBoard)

            if win_check(gameBoard, player1_marker):
                print('Congratulations! Player One has won.')
                game_on = False

            else:
                if full_board_check(gameBoard):
                    print('Its a draw')
                    break
                else:
                    turn = "Player 2"
        else:
            # player 2

            display_board(gameBoard)
            playerTwoMove = player_choice(gameBoard)

            print("JDFdnwnw")
            place_marker(gameBoard, player2_marker, playerTwoMove)
            display_board(gameBoard)


            if win_check(gameBoard, player2_marker):
                print('Congratulations! Player Two has won.')
                game_on = False

            else:
                if full_board_check(gameBoard):
                    print('Its a draw')
                    break
                else:
                    turn = "Player 1"
    if not replay():
        print('Thanks for playing')
        break
