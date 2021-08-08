from helper_functions import *
import sys


class ABGame:
    def __init__(self):
        self.count_pos = 0

    def a_b_MaxMinMidgame(self, board, depth, alpha, beta):
        if depth == 0:
            self.count_pos += 1
            return static_estimation_midgame(board), board

        else:
            v = -10**303
            L = GenerateMovesMidgameEndgame(board)
            if len(L) == 0:
              return static_estimation_midgame(board), board
            init_board = None
            for a_board in L:
                v_temp,new_board = self.a_b_MinMaxMidgame(a_board, depth-1, alpha, beta)
                if v_temp > v:
                    v = v_temp
                    init_board = a_board.copy()
                if v >= beta:
                    return v, init_board
                else:
                    alpha = max(v, alpha)
            return v, init_board

    def a_b_MinMaxMidgame(self, board, depth, alpha, beta):
        if depth == 0:
            self.count_pos += 1
            return static_estimation_midgame(board), board
        else:
            v = 10**303
            L = GenerateMovesMidgameEndgame(flip_board(board))
            if len(L) == 0:
              return static_estimation_midgame(flip_board(board)),flip_board(board)
            init_board = None
            for a_board in L:
                v_temp, new_board = self.a_b_MaxMinMidgame(flip_board(a_board), depth-1, alpha, beta)
                if v_temp < v:
                    v = v_temp
                    init_board = a_board.copy()
                if v <= alpha:
                    return v, init_board
                else:
                    beta = min(v, beta)
            return v, init_board


if __name__=='__main__':
    board_file = sys.argv[1]
    board_output = sys.argv[2]
    depth = int(sys.argv[3])
    with open(board_file, 'r') as f:
        board = f.readline()
    board = list(board)
    game = ABGame()
    static, next_move = game.a_b_MaxMinMidgame(board, depth, -10**299, 10**299)
    with open(board_output,'w') as f:
        f.write(''.join(next_move))
    print_the_board(next_move)
    print(f"Input position: {''.join(board)} Output position: {''.join(next_move)}")
    print("Positions evaluated by static estimation: ", game.count_pos)
    print("MINIMAX estimate: ",static)
