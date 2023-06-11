"""
Tic Tac Toe Player
"""

import math

from typing import List

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    XvsO = 0 # Positive for more X and negative for more Y
    for row in board:
        for item in row:
            if item == X:
                XvsO += 1
            elif item == O:
                XvsO -= 1

    if XvsO <= 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = list()

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == EMPTY:
                actions.append((i, j))

    return actions


def result(board: list, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_player = player(board=board)
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError
    new_board = initial_state()

    for i in range(0, 3):
        for j in range(0, 3):
            new_board[i][j] = board[i][j]

    new_board[action[0]][action[1]] = curr_player

    return new_board

def same(a, b, c):
    """
    Returns the element is all 3 are same element
    """
    if a == b == c != EMPTY:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #Check rows
    for row in board:
        if (same(*row)):
            return row[0]
        
    #Check columns
    temp = list()
    for i in range(0, 3):
        for j in range(0, 3):
            temp.append(board[j][i])
        if same(*temp):
            return temp[0]
        temp = list()
        
    # Check diagonal
    if same(board[0][0], board[1][1], board[2][2]):
        return board[0][0]
    
    # Check reverse diagonal
    if same(board[0][2], board[1][1], board[2][0]):
        return board[0][2]
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board=board):
        return True
    
    for row in board:
        for item in row:
            if item == EMPTY:
                return False
            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_symbol = winner(board=board)

    if winning_symbol == X:
        return 1
    elif winning_symbol == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    curr_player = player(board=board)
    player_actions = actions(board)

    opt_idx = -10
    if (curr_player == X):
        val = -1
    else:
        val = 1

    for i, action in enumerate(player_actions):
        minimax_search_val = minimax_search(result(board, action), val)
        if curr_player == X:
            if val < minimax_search_val:
                opt_idx = i
                val = minimax_search_val
        else:
            if val > minimax_search_val:
                opt_idx = i
                val = minimax_search_val

    return player_actions[opt_idx]

def minimax_search(board, purr):
    if terminal(board):
        return utility(board)

    curr_player = player(board=board)
    player_actions = actions(board=board)

    if (curr_player == X):
        val = -1
    else:
        val = 1

    for action in player_actions:
        board[action[0]][action[1]] = curr_player
        minimax_search_val = minimax_search(board, val)
        board[action[0]][action[1]] = EMPTY
        if curr_player == X:
            if minimax_search_val > purr:
                return minimax_search_val
            if val < minimax_search_val:
                val = minimax_search_val
        else:
            if minimax_search_val < purr:
                return minimax_search_val
            if val > minimax_search_val:
                val = minimax_search_val

    return val
