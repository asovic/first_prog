# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 19:19:54 2019

@author: Andrej
"""

def display_board(board):
    
    print('   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   '.format(board[7],board[8],board[9],board[4],board[5],board[6],board[1],board[2],board[3]))

real_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
demo_board = ['#','1','2','3','4','5','6','7','8','9']
############################################################
def player_input():
    marker = None
    while marker not in ('X','O'):
        marker = input('{}: Do you want to be X or O?'.format(starting_player)).upper()
    if marker == 'X':
        return ('X','O')            #Prva pozicija bo player1
    else:
        return ('O','X')
    pass
############################################################
def place_marker(board, marker, position):
    real_board[position] = marker
    pass
############################################################
def win_check(board, mark):
    return ((real_board[1] == mark and real_board[2] == mark and real_board[3] == mark) or
    (real_board[4] == mark and real_board[5] == mark and real_board[6] == mark) or
    (real_board[7] == mark and real_board[8] == mark and real_board[9] == mark) or
    (real_board[1] == mark and real_board[5] == mark and real_board[9] == mark) or
    (real_board[3] == mark and real_board[5] == mark and real_board[7] == mark) or
    (real_board[1] == mark and real_board[4] == mark and real_board[7] == mark) or
    (real_board[2] == mark and real_board[5] == mark and real_board[8] == mark) or
    (real_board[3] == mark and real_board[6] == mark and real_board[9] == mark))
    pass
############################################################
import random

def choose_first():
    first_player = random.randint(1,2)
    if first_player == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    pass
############################################################
def space_check(board, position):
    return real_board[position] == ' '
    pass

############################################################
def full_board_check(board):
    return ' ' not in real_board
    pass
############################################################
def player_choice(board):
    position = int(input('Choose your position from 1 to 9: '))
    while not space_check(real_board,position) or position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input('Position {} is already taken, choose another one: '.format(position)))
    return position
    pass
############################################################
def replay():
    rerun = None
    while rerun not in ('yes','no'):
        rerun = input('Do you want to play again?').lower()
    return rerun == 'yes'
    pass
############################################################

while True:
    game_on = True
    real_board = [' ']*10 #Vedno začne s prazno tablo
    display_board(demo_board) #Prikaže board in kje so pozicije
    starting_player = choose_first() #Kdo gre prvi
    print('Computer decided that '+ starting_player +' will go first.')
    if starting_player == 'Player 1':
        p1_marker,p2_marker = player_input()
    else:
        p2_marker,p1_marker = player_input()
    while game_on:
        if starting_player == 'Player 1':
            display_board(real_board)
            position = player_choice(real_board) #Player 1 izbere pozicijo
            place_marker(real_board,p1_marker,position) #Vnese marker na izbrano pozicijo
            if win_check(real_board,p1_marker) == True: #Preveri če je na tabli zmagovalna kombinacija
                display_board(real_board)
                print('Congratulations! \nPlayer 1 has won the game!')
                game_on = False #Prekine while loop
            else:
                if full_board_check(real_board):
                    display_board(real_board)
                    print('It\'s a TIE.')
                    game_on = False
                else:
                    starting_player = 'Player 2'
        else:
            display_board(real_board)
            position = player_choice(real_board)
            place_marker(real_board,p2_marker,position)
            if win_check(real_board,p2_marker) == True:
                display_board(real_board)
                print('Congratulations! \nPlayer 2 has won the game!')
                game_on = False
            else:
                if full_board_check(real_board) == True:
                    display_board(real_board)
                    print('It\'s a TIE.')
                    game_on = False
                else:
                    starting_player = 'Player 1'
    if not replay():
        break