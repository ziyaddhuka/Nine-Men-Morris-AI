from helper_functions import *
import sys

class MiniMaxGameImproved:
    def __init__(self):
        self.count_pos = 0

    def new_MaxMinMidgame(self, board, depth):
        if depth == 0:
            self.count_pos = self.count_pos + 1
            return improved_static_midgame(board), board
        else:
            v = -10**305
            L = GenerateMovesMidgameEndgame(board)
            if len(L) == 0:
              return static_estimation_midgame((board)),(board)
            init_board = None
            for a_board in L:
                v_temp,new_board = self.new_MinMaxMidgame(a_board, depth-1)
                if v_temp > v:
                    v = v_temp
                    init_board = a_board.copy()
            # v = max(v, MinMax(a_board, depth-1))
            return v, init_board

    def new_MinMaxMidgame(self, board, depth):
        if depth == 0:
            self.count_pos = self.count_pos + 1
            return improved_static_midgame(board), board
        else:
            v = 10**305
            L = GenerateMovesMidgameEndgame(flip_board(board))
            if len(L) == 0:
              return static_estimation_midgame((board)),flip_board(board)
            init_board = None
            for a_board in L:
                v_temp, new_board = self.new_MaxMinMidgame(flip_board(a_board), depth-1)
                if v_temp < v:
                    v = v_temp
                    init_board = a_board.copy()
            # v = min(v, MaxMin(flip_board(a_board), depth-1))
        return v, init_board



if __name__=='__main__':
    board_file = sys.argv[1]
    board_output = sys.argv[2]
    depth = int(sys.argv[3])
    with open('board.txt', 'r') as f:
        board = f.readline()
    board = list(board)
    game = MiniMaxGameImproved()
    static, next_move = game.new_MaxMinMidgame(board, depth)
    with open(board_output,'w') as f:
        f.write(''.join(next_move))
    print_the_board(next_move)
    print(f"Input position: {''.join(board)} Output position: {''.join(next_move)}")
    print("Positions evaluated by static estimation: ", game.count_pos)
    print("MINIMAX estimate: ",static)
