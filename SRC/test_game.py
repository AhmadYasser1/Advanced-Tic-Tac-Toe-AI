import pytest

from tic_tac_toe import *

# Creating the game instances
ttt = TicTacToe()

random.seed(None)


def gen_state(to_move='X', x_positions=[], o_positions=[]):
    """Given whose turn it is to move, the positions of X's on the board, and the
    positions of O's on the board,return the corresponding
    game state"""

    moves = set([(x, y) for x in range(1, 4) for y in range(1, 4)]) - set(x_positions) - set(o_positions)
    moves = list(moves)
    board = {}
    for pos in x_positions:
        board[pos] = 'X'
    for pos in o_positions:
        board[pos] = 'O'
    return GameState(to_move=to_move, utility=0, board=board, moves=moves)


def test_alpha_beta_search():

    state = gen_state(to_move='X', x_positions=[(1, 1), (3, 3)],
                      o_positions=[(1, 2), (3, 2)])
    assert alpha_beta_search(state, ttt) == (2, 2)

    state = gen_state(to_move='O', x_positions=[(1, 1), (3, 1), (3, 3)],
                      o_positions=[(1, 2), (3, 2)])
    assert alpha_beta_search(state, ttt) == (2, 2)

    state = gen_state(to_move='O', x_positions=[(1, 1)],
                      o_positions=[])
    assert alpha_beta_search(state, ttt) == (2, 2)

    state = gen_state(to_move='X', x_positions=[(1, 1), (3, 1)],
                      o_positions=[(2, 2), (3, 1)])
    assert alpha_beta_search(state, ttt) == (1, 3)

    return


def test_random_tests():

    # The player 'X' (one who plays first) in TicTacToe never loses:
    assert ttt.play_game(alpha_beta_player, alpha_beta_player) >= 0

    # The player 'X' (one who plays first) in TicTacToe never loses:
    assert ttt.play_game(alpha_beta_player, random_player) >= 0

    # The player 'X' (one who plays first) in TicTacToe never loses:
    assert ttt.play_game(alpha_beta_player, minmax_player) >= 0

    return

if __name__ == "__main__":
    pytest.main()