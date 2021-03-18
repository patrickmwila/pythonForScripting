#!/usr/bin/python3
# Using Data Structures to Model Real-World Things
# A tic-tac-toe board is modeled here

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'                                            #set turn equal to X for player 1
for i in range(9):                                    # run this code for nine times
    printBoard(theBoard)
    print(f'\nTurn for {turn}. Move on which space?') # ask current player to move 
    move = input()                                    # store the players move in move_variable
    theBoard[move] = turn                             # update theBoard with move as key and current turn as value

    if turn == 'X':                                   # make sure turn is updated
        turn = 'O'
    else:
        turn = 'X'


printBoard(theBoard)
