from tictactoe import EMPTY, X, O
from tictactoe import initial_state, player, result, minimax_search

def test_initial_state():
    assert initial_state() == [[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]

def test_player():
    board = initial_state()
    assert player(board=board) == X
    board[0][0] = X
    assert player(board) == O
    board[0][1] = O
    assert player(board) == X

def test_result():
    board = initial_state()
    board2 = initial_state()
    board3 = result(board, (0, 0))
    assert board == board2
    board2[0][0] = X
    assert board3 == board2