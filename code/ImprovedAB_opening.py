from helper_functions import *
import sys


class ABOpening:
    def __init__(self):
        self.count_pos = 0

    def imp_a_b_MaxMin(self, board, depth, alpha, beta):
        if depth == 0:
            self.count_pos += 1
          # print("Max returns ", static_estimation_opening(board))
            return improved_static(board), board
        else:
            v = -10**305
            L = GenerateMovesOpening(board)

            init_board = None
            for a_board in L:
                v_temp,new_board = self.imp_a_b_MinMax(a_board, depth-1, alpha, beta)
                if v_temp > v:
                    v = v_temp
                    init_board = a_board.copy()
                if v >= beta:
                    return v, init_board
                else:
                    alpha = max(v, alpha)
            # v = max(v, MinMax(a_board, depth-1))
            return v, init_board



    def imp_a_b_MinMax(self, board, depth, alpha, beta):
        if depth == 0:
            self.count_pos += 1
          # print("Min Returns", static_estimation_opening(board))
            return improved_static(board), board
        else:
            v = 10**305
            L = GenerateMovesOpening(flip_board(board))
            init_board = None
            for a_board in L:
                v_temp, new_board = self.imp_a_b_MaxMin(flip_board(a_board), depth-1, alpha, beta)
                if v_temp < v:
                    v = v_temp
                    init_board = a_board.copy()
                if v <= alpha:
                    return v, init_board
                else:
                    beta = min(v, beta)
            # v = min(v, MaxMin(flip_board(a_board), depth-1))
            return v, init_board



if __name__=='__main__':
    board_file = sys.argv[1]
    board_output = sys.argv[2]
    depth = int(sys.argv[3])
    with open(board_file, 'r') as f:
        board = f.readline()
    board = list(board)
    print_the_board(board)
    game = ABOpening()
    static, next_move = game.imp_a_b_MaxMin(board, depth, -10**299, 10**299)
    with open(board_output,'w') as f:
        f.write(''.join(next_move))
    print_the_board(next_move)
    print(f"Input position: {''.join(board)} Output position: {''.join(next_move)}")
    print("Positions evaluated by static estimation: ", game.count_pos)
    print("MINIMAX estimate: ",static)
